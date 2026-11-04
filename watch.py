"""GlobalFeed License Watch.

Checks the licenses of open models on Hugging Face once a day and records
every change. For each tracked organisation it follows the most downloaded
and the newest models, stores the license tag and the full LICENSE file,
and writes a dated entry whenever either one changes.

Standard library only. Run:  python watch.py
Optional: set HF_TOKEN to read gated repositories.
"""
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
TEXTS = DATA / "licenses"
STATE = DATA / "models.json"
CHANGELOG = ROOT / "CHANGES.md"
RELEASE_NOTES = ROOT / "release-notes.md"
README = ROOT / "README.md"
API = "https://huggingface.co/api"
TOKEN = os.environ.get("HF_TOKEN", "")
LICENSE_FILE = re.compile(r"^(LICEN[CS]E|LICEN[CS]E[._-].*|.*license.*\.(txt|md))$", re.I)


def get(url, raw=False):
    headers = {"User-Agent": "globalfeed-license-watch"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
        body = r.read()
    return body.decode("utf-8", "replace") if raw else json.loads(body)


def tracked_models(org, per_list):
    """Most downloaded plus newest models of an organisation, without duplicates."""
    ids = []
    for sort in ("downloads", "createdAt"):
        for m in get(f"{API}/models?author={org}&sort={sort}&direction=-1&limit={per_list}"):
            if m["id"] not in ids:
                ids.append(m["id"])
    return ids


def read_model(model_id):
    info = get(f"{API}/models/{model_id}")
    tags = [t.split(":", 1)[1] for t in info.get("tags", []) if t.startswith("license:")]
    card = info.get("cardData") or {}
    files = [s["rfilename"] for s in info.get("siblings", []) if "/" not in s["rfilename"]]
    lic_file = next((f for f in files if LICENSE_FILE.match(f)), None)
    text = None
    if lic_file:
        try:
            text = get(f"https://huggingface.co/{model_id}/resolve/main/{lic_file}", raw=True)
        except urllib.error.HTTPError as e:
            text = None if e.code in (401, 403) else ""
    return {
        "license": tags[0] if tags else card.get("license"),
        "license_name": card.get("license_name"),
        "license_file": lic_file,
        "license_sha256": hashlib.sha256(text.encode()).hexdigest() if text else None,
        "gated": bool(info.get("gated")),
        "created": (info.get("createdAt") or "")[:10],
    }, text


def text_path(model_id):
    return TEXTS / f"{model_id}.txt"


def describe(model_id, old, new):
    parts = []
    if old["license"] != new["license"]:
        parts.append(f"license tag `{old['license']}` → `{new['license']}`")
    if old.get("license_sha256") != new.get("license_sha256") and new.get("license_sha256"):
        parts.append(f"`{new['license_file']}` text changed" if old.get("license_sha256") else f"`{new['license_file']}` added")
    return f"- **{model_id}**: " + "; ".join(parts) if parts else None


def render_readme(state):
    rows = ["| Organisation | Model | License | License file | Last change |", "|---|---|---|---|---|"]
    for mid in sorted(state, key=str.lower):
        m = state[mid]
        lic = m["license"] or "not set"
        if m.get("license_name"):
            lic += f" ({m['license_name']})"
        f = f"[{m['license_file']}](data/licenses/{mid}.txt)" if text_path(mid).exists() else (m["license_file"] or "none")
        if m.get("gated") and not text_path(mid).exists() and m["license_file"]:
            f += " (gated)"
        rows.append(f"| {mid.split('/')[0]} | [{mid.split('/')[1]}](https://huggingface.co/{mid}) | {lic} | {f} | {m.get('changed') or '-'} |")
    table = "\n".join(rows)
    text = README.read_text(encoding="utf-8")
    start, end = "<!-- table:start -->", "<!-- table:end -->"
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    block = f"{start}\n_Last checked: {updated} · {len(state)} models_\n\n{table}\n{end}"
    README.write_text(re.sub(f"{start}.*?{end}", block, text, flags=re.S), encoding="utf-8")


def main():
    config = json.loads((ROOT / "orgs.json").read_text(encoding="utf-8"))
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    changes, errors = [], []

    for org in config["orgs"]:
        known = [m for m in state if m.split("/")[0] == org]  # once tracked, always rechecked
        try:
            ids = tracked_models(org, config["per_list"])
        except Exception as e:  # one failing organisation must not stop the run
            errors.append(f"{org}: {e}")
            ids = []
        ids += [m for m in known if m not in ids]
        for mid in ids:
            try:
                new, text = read_model(mid)
            except Exception as e:
                errors.append(f"{mid}: {e}")
                continue
            old = state.get(mid)
            if text:
                p = text_path(mid)
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text, encoding="utf-8")
            if old is None:  # newly tracked models are not changes; only later edits count
                new["first_seen"] = today
                new["changed"] = None
            else:
                line = describe(mid, old, new)
                new["first_seen"] = old.get("first_seen", today)
                new["changed"] = today if line else old.get("changed")
                if line:
                    changes.append(line)
            state[mid] = new

    DATA.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    render_readme(state)

    if changes:
        entry = f"## {today}\n\n" + "\n".join(changes) + "\n"
        old_log = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else "# License changes\n"
        head, _, rest = old_log.partition("\n")
        CHANGELOG.write_text(f"{head}\n\n{entry}{rest}", encoding="utf-8")
        RELEASE_NOTES.write_text(entry, encoding="utf-8")
    elif RELEASE_NOTES.exists():
        RELEASE_NOTES.unlink()

    print(f"{len(state)} models, {len(changes)} changes, {len(errors)} errors")
    for e in errors:
        print("  error:", e, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
