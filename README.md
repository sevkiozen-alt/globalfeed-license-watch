# GlobalFeed License Watch

Open model licenses change quietly. A model that shipped under MIT can come back with new terms for API providers, a usage policy or a name-display clause, and most people only notice months later.

This repository checks the licenses of open models on Hugging Face every day and keeps a public, dated record of every change.

## What it tracks

- The four most downloaded and the four newest models of each organisation in [`orgs.json`](orgs.json). Once a model is tracked, it keeps being checked.
- The license tag on the model page and the full text of the model's `LICENSE` file.
- A change is recorded when either the tag or the license text changes.

## Where to look

- **Current licenses:** the table below, refreshed every day.
- **Full license texts:** [`data/licenses/`](data/licenses), one file per model. Git history shows every earlier version.
- **Change log:** [`CHANGES.md`](CHANGES.md).
- **Machine-readable data:** [`data/models.json`](data/models.json).

## Get notified

Each day with at least one change becomes a GitHub release.

- Click **Watch → Custom → Releases** at the top of this page to get an email for every change.
- Or follow the feed in any RSS reader: `https://github.com/sevkiozen-alt/globalfeed-license-watch/releases.atom`

## Using the data

Nothing to install and no API key needed. Everything is plain files in this repository.

- **Read in a browser:** the table below, with a link to each license text.
- **Use in your own code:** fetch `https://raw.githubusercontent.com/sevkiozen-alt/globalfeed-license-watch/main/data/models.json`. It is a static JSON file updated daily, so no account or token is required.
- **Track other organisations:** fork the repository and edit `orgs.json`. The daily check then runs in your fork through GitHub Actions.

## Run it yourself

```bash
python watch.py
```

Python 3.10 or newer, no dependencies. Set `HF_TOKEN` to also read license files of gated repositories. To track another organisation, add its Hugging Face name to `orgs.json`.

## Current licenses

<!-- table:start -->
_Last checked: 2026-11-09 · 166 models_

| Organisation | Model | License | License file | Last change |
|---|---|---|---|---|
| allenai | [AstaBrief_8B_SFT](https://huggingface.co/allenai/AstaBrief_8B_SFT) | apache-2.0 | none | - |
| allenai | [HiRO-ACEv2](https://huggingface.co/allenai/HiRO-ACEv2) | apache-2.0 | none | - |
| allenai | [longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) | apache-2.0 | none | - |
| allenai | [maniflow-tb](https://huggingface.co/allenai/maniflow-tb) | apache-2.0 | [LICENSE](data/licenses/allenai/maniflow-tb.txt) | - |
| allenai | [Molmo2-4B-tb](https://huggingface.co/allenai/Molmo2-4B-tb) | apache-2.0 | none | - |
| allenai | [Olmo-3-7B-Instruct](https://huggingface.co/allenai/Olmo-3-7B-Instruct) | apache-2.0 | none | - |
| allenai | [olmOCR-7B-0825-FP8](https://huggingface.co/allenai/olmOCR-7B-0825-FP8) | apache-2.0 | none | - |
| allenai | [OlmoEarth-v1_2-FT-LFMC-Base](https://huggingface.co/allenai/OlmoEarth-v1_2-FT-LFMC-Base) | other (olmoearth-artifact-license) | [LICENSE.txt](data/licenses/allenai/OlmoEarth-v1_2-FT-LFMC-Base.txt) | - |
| allenai | [OlmoEarth-v1_3-Base](https://huggingface.co/allenai/OlmoEarth-v1_3-Base) | other | [LICENSE.txt](data/licenses/allenai/OlmoEarth-v1_3-Base.txt) | - |
| allenai | [scibert_scivocab_uncased](https://huggingface.co/allenai/scibert_scivocab_uncased) | not set | none | - |
| allenai | [specter2_base](https://huggingface.co/allenai/specter2_base) | apache-2.0 | none | - |
| baidu | [ERNIE-4.5-21B-A3B-Thinking](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-Thinking) | apache-2.0 | [LICENSE](data/licenses/baidu/ERNIE-4.5-21B-A3B-Thinking.txt) | - |
| baidu | [ERNIE-5.5-Flash-Base](https://huggingface.co/baidu/ERNIE-5.5-Flash-Base) | other (ernie-5.5-flash-base-model-license-v1.0) | [LICENSE](data/licenses/baidu/ERNIE-5.5-Flash-Base.txt) | - |
| baidu | [ERNIE-5.5-Flash-Base-BF16](https://huggingface.co/baidu/ERNIE-5.5-Flash-Base-BF16) | other (ernie-5.5-flash-base-model-license-v1.0) | [LICENSE](data/licenses/baidu/ERNIE-5.5-Flash-Base-BF16.txt) | - |
| baidu | [ERNIE-Image-Aes](https://huggingface.co/baidu/ERNIE-Image-Aes) | apache-2.0 | none | - |
| baidu | [NAVA](https://huggingface.co/baidu/NAVA) | apache-2.0 | [LICENSE](data/licenses/baidu/NAVA.txt) | - |
| baidu | [Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR) | apache-2.0 | [LICENSE](data/licenses/baidu/Qianfan-OCR.txt) | - |
| baidu | [Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) | mit | [LICENSE](data/licenses/baidu/Unlimited-OCR.txt) | - |
| baidu | [Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2) | mit | none | - |
| black-forest-labs | [flux-3-image-klein](https://huggingface.co/black-forest-labs/flux-3-image-klein) | other (flux-kommunity-license) | [LICENSE.md](data/licenses/black-forest-labs/flux-3-image-klein.txt) | - |
| black-forest-labs | [flux-3-image-klein-base](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) | other (flux-kommunity-license) | [LICENSE.md](data/licenses/black-forest-labs/flux-3-image-klein-base.txt) | - |
| black-forest-labs | [flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) | other (flux-kommunity-license) | [LICENSE.md](data/licenses/black-forest-labs/flux-3-image-klein-comfy.txt) | - |
| black-forest-labs | [flux-3-image-klein-pup](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup) | apache-2.0 | none | - |
| black-forest-labs | [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) | other (flux-1-dev-non-commercial-license) | [LICENSE.md](data/licenses/black-forest-labs/FLUX.1-dev.txt) | - |
| black-forest-labs | [FLUX.2-klein-4b-fp8](https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-fp8) | apache-2.0 | [LICENSE.md](data/licenses/black-forest-labs/FLUX.2-klein-4b-fp8.txt) | - |
| black-forest-labs | [FLUX.2-klein-base-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B) | apache-2.0 | [LICENSE.md](data/licenses/black-forest-labs/FLUX.2-klein-base-4B.txt) | - |
| ByteDance-Seed | [Cola2](https://huggingface.co/ByteDance-Seed/Cola2) | not set | none | - |
| ByteDance-Seed | [Cross-Layer-TopK-CLT](https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT) | apache-2.0 | [LICENSE](data/licenses/ByteDance-Seed/Cross-Layer-TopK-CLT.txt) | - |
| ByteDance-Seed | [GenFirst](https://huggingface.co/ByteDance-Seed/GenFirst) | cc-by-nc-4.0 | [LICENSE](data/licenses/ByteDance-Seed/GenFirst.txt) | - |
| ByteDance-Seed | [PAR](https://huggingface.co/ByteDance-Seed/PAR) | apache-2.0 | none | - |
| ByteDance-Seed | [Qwen3-30B-A3B-MoE-SAE](https://huggingface.co/ByteDance-Seed/Qwen3-30B-A3B-MoE-SAE) | apache-2.0 | [LICENSE](data/licenses/ByteDance-Seed/Qwen3-30B-A3B-MoE-SAE.txt) | - |
| ByteDance-Seed | [Seed-OSS-36B-Instruct](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct) | apache-2.0 | [LICENSE.txt](data/licenses/ByteDance-Seed/Seed-OSS-36B-Instruct.txt) | - |
| ByteDance-Seed | [SeedVR2-3B](https://huggingface.co/ByteDance-Seed/SeedVR2-3B) | apache-2.0 | none | - |
| ByteDance-Seed | [SeedVR2-7B](https://huggingface.co/ByteDance-Seed/SeedVR2-7B) | apache-2.0 | none | - |
| ByteDance-Seed | [SimArt](https://huggingface.co/ByteDance-Seed/SimArt) | apache-2.0 | none | - |
| ByteDance-Seed | [TaskMem](https://huggingface.co/ByteDance-Seed/TaskMem) | apache-2.0 | none | - |
| ByteDance-Seed | [UI-TARS-1.5-7B](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B) | apache-2.0 | none | - |
| deepseek-ai | [DeepSeek-OCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-OCR.txt) | - |
| deepseek-ai | [DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-V3.2.txt) | - |
| deepseek-ai | [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-V4-Flash-0731.txt) | - |
| deepseek-ai | [DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp.txt) | - |
| deepseek-ai | [DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-V4-Pro-0813.txt) | - |
| deepseek-ai | [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-V4.1-Flash.txt) | - |
| deepseek-ai | [DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | mit | [LICENSE](data/licenses/deepseek-ai/DeepSeek-V4.1-Flash-1017.txt) | - |
| google | [electra-base-discriminator](https://huggingface.co/google/electra-base-discriminator) | apache-2.0 | none | - |
| google | [embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) | apache-2.0 | none | - |
| google | [gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) | apache-2.0 | none | - |
| google | [gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | apache-2.0 | none | - |
| google | [gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it) | apache-2.0 | none | - |
| google | [gnm-v3](https://huggingface.co/google/gnm-v3) | apache-2.0 | none | - |
| google | [timesfm-3.0-pytorch](https://huggingface.co/google/timesfm-3.0-pytorch) | other (timesfm-non-commercial-license-v1.0) | [LICENSE](data/licenses/google/timesfm-3.0-pytorch.txt) | - |
| google | [tipsv1-g14-lowres](https://huggingface.co/google/tipsv1-g14-lowres) | apache-2.0 | none | - |
| google | [vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) | apache-2.0 | none | - |
| ibm-granite | [granite-4.1-3b](https://huggingface.co/ibm-granite/granite-4.1-3b) | apache-2.0 | none | - |
| ibm-granite | [granite-embedding-small-english-r2](https://huggingface.co/ibm-granite/granite-embedding-small-english-r2) | apache-2.0 | none | - |
| ibm-granite | [granite-speech-5.0-2b-ONNX](https://huggingface.co/ibm-granite/granite-speech-5.0-2b-ONNX) | apache-2.0 | none | - |
| ibm-granite | [granite-switch-4.1-30b-GGUF](https://huggingface.co/ibm-granite/granite-switch-4.1-30b-GGUF) | apache-2.0 | none | - |
| ibm-granite | [granite-switch-4.1-8b](https://huggingface.co/ibm-granite/granite-switch-4.1-8b) | apache-2.0 | none | - |
| ibm-granite | [granite-switch-4.1-8b-GGUF](https://huggingface.co/ibm-granite/granite-switch-4.1-8b-GGUF) | apache-2.0 | none | - |
| ibm-granite | [granite-timeseries-tspulse-r1](https://huggingface.co/ibm-granite/granite-timeseries-tspulse-r1) | apache-2.0 | none | - |
| ibm-granite | [granite-timeseries-ttm-r3](https://huggingface.co/ibm-granite/granite-timeseries-ttm-r3) | apache-2.0 | none | - |
| LiquidAI | [d1-2B-GGUF](https://huggingface.co/LiquidAI/d1-2B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/d1-2B-GGUF.txt) | - |
| LiquidAI | [d1-Omni-2B-GGUF](https://huggingface.co/LiquidAI/d1-Omni-2B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/d1-Omni-2B-GGUF.txt) | - |
| LiquidAI | [LFM2.5-2.6B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-2.6B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM2.5-2.6B-GGUF.txt) | - |
| LiquidAI | [LFM2.5-230M-Base](https://huggingface.co/LiquidAI/LFM2.5-230M-Base) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM2.5-230M-Base.txt) | - |
| LiquidAI | [LFM2.5-Audio-1.5B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM2.5-Audio-1.5B-GGUF.txt) | - |
| LiquidAI | [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF.txt) | - |
| LiquidAI | [LFM3-1.7B-GGUF](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM3-1.7B-GGUF.txt) | - |
| LiquidAI | [LFM3-1.7B-MLX-5bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-5bit) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM3-1.7B-MLX-5bit.txt) | - |
| LiquidAI | [LFM3-Audio-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-Audio-2B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM3-Audio-2B-GGUF.txt) | - |
| LiquidAI | [LFM3-Omni-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-Omni-2B-GGUF) | other (lfm1.0) | [LICENSE](data/licenses/LiquidAI/LFM3-Omni-2B-GGUF.txt) | - |
| meta-llama | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | llama3.1 | [LICENSE](data/licenses/meta-llama/Llama-3.1-8B-Instruct.txt) | - |
| meta-llama | [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | llama3.2 | [LICENSE.txt](data/licenses/meta-llama/Llama-3.2-1B-Instruct.txt) | - |
| meta-llama | [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | llama3.2 | [LICENSE.txt](data/licenses/meta-llama/Llama-3.2-3B-Instruct.txt) | - |
| meta-llama | [Llama-4-Maverick-17B-128E-Instruct-FP8-Original](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-Original) | other (llama4) | [LICENSE](data/licenses/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-Original.txt) | - |
| meta-llama | [Llama-Guard-4-12B](https://huggingface.co/meta-llama/Llama-Guard-4-12B) | other (llama4) | [LICENSE](data/licenses/meta-llama/Llama-Guard-4-12B.txt) | - |
| meta-llama | [Llama-Prompt-Guard-2-22M](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M) | other (llama4) | [LICENSE](data/licenses/meta-llama/Llama-Prompt-Guard-2-22M.txt) | - |
| meta-llama | [Llama-Prompt-Guard-2-86M](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M) | other (llama4) | [LICENSE](data/licenses/meta-llama/Llama-Prompt-Guard-2-86M.txt) | - |
| meta-llama | [Prompt-Guard-86M](https://huggingface.co/meta-llama/Prompt-Guard-86M) | llama3.1 | [LICENSE](data/licenses/meta-llama/Prompt-Guard-86M.txt) | - |
| microsoft | [Florence-2-base](https://huggingface.co/microsoft/Florence-2-base) | mit | [LICENSE](data/licenses/microsoft/Florence-2-base.txt) | - |
| microsoft | [Mage-VL-Cowork](https://huggingface.co/microsoft/Mage-VL-Cowork) | apache-2.0 | [LICENSE](data/licenses/microsoft/Mage-VL-Cowork.txt) | - |
| microsoft | [mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) | mit | none | - |
| microsoft | [scFM-dataselection](https://huggingface.co/microsoft/scFM-dataselection) | mit | [LICENSE](data/licenses/microsoft/scFM-dataselection.txt) | - |
| microsoft | [Sentiment-Analysis-7B](https://huggingface.co/microsoft/Sentiment-Analysis-7B) | mit | none | - |
| microsoft | [TRELLIS-image-large](https://huggingface.co/microsoft/TRELLIS-image-large) | mit | none | - |
| microsoft | [TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B) | mit | none | - |
| microsoft | [UserRepGen-4B](https://huggingface.co/microsoft/UserRepGen-4B) | mit | [LICENSE.Qwen](data/licenses/microsoft/UserRepGen-4B.txt) | - |
| MiniMaxAI | [MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | other (minimax-h3-community-license-agreement) | [LICENSE](data/licenses/MiniMaxAI/MiniMax-H3.txt) | - |
| MiniMaxAI | [MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) | other (modified-mit) | [LICENSE-MODEL](data/licenses/MiniMaxAI/MiniMax-M2.5.txt) | - |
| MiniMaxAI | [MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) | other (other) | [LICENSE](data/licenses/MiniMaxAI/MiniMax-M2.7.txt) | - |
| MiniMaxAI | [MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) | other (minimax-community) | [LICENSE](data/licenses/MiniMaxAI/MiniMax-M3.txt) | - |
| MiniMaxAI | [MiniMax-M3-MXFP8](https://huggingface.co/MiniMaxAI/MiniMax-M3-MXFP8) | other (minimax-community) | [LICENSE](data/licenses/MiniMaxAI/MiniMax-M3-MXFP8.txt) | - |
| MiniMaxAI | [MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | other (minimax-community) | [LICENSE](data/licenses/MiniMaxAI/MiniMax-M3.1-Flash.txt) | - |
| MiniMaxAI | [MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3) | not set | [LICENSE](data/licenses/MiniMaxAI/MiniMax-Music3.txt) | - |
| mistralai | [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) | apache-2.0 | none | - |
| mistralai | [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | apache-2.0 | none | - |
| mistralai | [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) | apache-2.0 | none | - |
| mistralai | [Mistral-Large-4-1T-A52B-NVFP4](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B-NVFP4) | other | [LICENSE](data/licenses/mistralai/Mistral-Large-4-1T-A52B-NVFP4.txt) | - |
| mistralai | [Timestral-123M](https://huggingface.co/mistralai/Timestral-123M) | other | [LICENSE](data/licenses/mistralai/Timestral-123M.txt) | - |
| mistralai | [Timestral-28M](https://huggingface.co/mistralai/Timestral-28M) | other | [LICENSE](data/licenses/mistralai/Timestral-28M.txt) | - |
| mistralai | [Timestral-5M](https://huggingface.co/mistralai/Timestral-5M) | other | [LICENSE](data/licenses/mistralai/Timestral-5M.txt) | - |
| mistralai | [Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) | apache-2.0 | none | - |
| moonshotai | [Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | other (modified-mit) | [LICENSE](data/licenses/moonshotai/Kimi-K2-Instruct.txt) | - |
| moonshotai | [Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5) | other (modified-mit) | [LICENSE](data/licenses/moonshotai/Kimi-K2.5.txt) | - |
| moonshotai | [Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) | other (modified-mit) | [LICENSE](data/licenses/moonshotai/Kimi-K2.6.txt) | - |
| moonshotai | [Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | other (modified-mit) | [LICENSE](data/licenses/moonshotai/Kimi-K2.7-Code.txt) | - |
| moonshotai | [Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) | other (kimi-k3) | [LICENSE](data/licenses/moonshotai/Kimi-K3.txt) | - |
| moonshotai | [Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | other (kimi-k3.1-pro) | [LICENSE](data/licenses/moonshotai/Kimi-K3.1-Pro.txt) | - |
| nvidia | [bigvgan_v2_22khz_80band_256x](https://huggingface.co/nvidia/bigvgan_v2_22khz_80band_256x) | mit | [LICENSE](data/licenses/nvidia/bigvgan_v2_22khz_80band_256x.txt) | - |
| nvidia | [DeepSeek-V4.1-Flash-1017-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4) | mit | [LICENSE](data/licenses/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4.txt) | - |
| nvidia | [Gemma-4-26B-A4B-NVFP4](https://huggingface.co/nvidia/Gemma-4-26B-A4B-NVFP4) | apache-2.0 (apache-license-2.0) | none | - |
| nvidia | [InternVideo2-CLIP-anomaly-detection](https://huggingface.co/nvidia/InternVideo2-CLIP-anomaly-detection) | other (nvidia-internal-scientific-research-and-development-model-license) | none | - |
| nvidia | [Metatron-v1](https://huggingface.co/nvidia/Metatron-v1) | other (nvidia-open-model-license) | [LICENSE.pdf](data/licenses/nvidia/Metatron-v1.txt) | - |
| nvidia | [MetricTrail](https://huggingface.co/nvidia/MetricTrail) | other (nvidia-open-model-license) | none | - |
| nvidia | [MotionBricks](https://huggingface.co/nvidia/MotionBricks) | not set | none | - |
| nvidia | [NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16) | other (nvidia-nemotron-open-model-license) | none | - |
| nvidia | [NVIDIA-Nemotron-3-Nano-4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16) | other (nvidia-nemotron-open-model-license) | LICENSE | - |
| nvidia | [Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | apache-2.0 | none | - |
| openai | [circuit-sparsity](https://huggingface.co/openai/circuit-sparsity) | apache-2.0 | [LICENSE.MD](data/licenses/openai/circuit-sparsity.txt) | - |
| openai | [clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) | not set | none | - |
| openai | [clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | not set | none | - |
| openai | [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | apache-2.0 | [LICENSE](data/licenses/openai/gpt-oss-20b.txt) | - |
| openai | [gpt-oss-safeguard-120b](https://huggingface.co/openai/gpt-oss-safeguard-120b) | apache-2.0 | [LICENSE](data/licenses/openai/gpt-oss-safeguard-120b.txt) | - |
| openai | [gpt-oss-safeguard-20b](https://huggingface.co/openai/gpt-oss-safeguard-20b) | apache-2.0 | [LICENSE](data/licenses/openai/gpt-oss-safeguard-20b.txt) | - |
| openai | [privacy-filter](https://huggingface.co/openai/privacy-filter) | apache-2.0 | none | - |
| openai | [whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) | mit | none | - |
| Qwen | [Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) | other (qwen-research) | [LICENSE](data/licenses/Qwen/Qwen-Image-2.1.txt) | - |
| Qwen | [Qwen-Image-2.1-PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) | other (qwen-research) | [LICENSE](data/licenses/Qwen/Qwen-Image-2.1-PE-I2I.txt) | - |
| Qwen | [Qwen-Image-2.1-PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I) | other (qwen-research) | [LICENSE](data/licenses/Qwen/Qwen-Image-2.1-PE-T2I.txt) | - |
| Qwen | [Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) | other (qwen-research) | [LICENSE](data/licenses/Qwen/Qwen-Image-2.1-Turbo.txt) | - |
| Qwen | [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | apache-2.0 | [LICENSE](data/licenses/Qwen/Qwen3-0.6B.txt) | - |
| Qwen | [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | apache-2.0 | [LICENSE](data/licenses/Qwen/Qwen3-14B.txt) | - |
| Qwen | [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) | apache-2.0 | [LICENSE](data/licenses/Qwen/Qwen3-4B.txt) | - |
| Qwen | [Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | apache-2.0 | none | - |
| Qwen | [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | apache-2.0 | [LICENSE](data/licenses/Qwen/Qwen3.8-27B.txt) | - |
| stabilityai | [SAME-L](https://huggingface.co/stabilityai/SAME-L) | other (stable-audio-community) | [LICENSE.md](data/licenses/stabilityai/SAME-L.txt) | - |
| stabilityai | [sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | not set | [LICENSE.md](data/licenses/stabilityai/sd-turbo.txt) | - |
| stabilityai | [sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | mit | none | - |
| stabilityai | [sdxl-base-amdnpu-medusa](https://huggingface.co/stabilityai/sdxl-base-amdnpu-medusa) | openrail++ | [LICENSE](data/licenses/stabilityai/sdxl-base-amdnpu-medusa.txt) | 2026-11-09 |
| stabilityai | [sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | other (sai-nc-community) | [LICENSE.md](data/licenses/stabilityai/sdxl-turbo.txt) | - |
| stabilityai | [stable-audio-3-optimized](https://huggingface.co/stabilityai/stable-audio-3-optimized) | other (stable-audio-community) | [LICENSE.md](data/licenses/stabilityai/stable-audio-3-optimized.txt) | - |
| stabilityai | [stable-diffusion-3.5-medium-amdnpu-medusa](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium-amdnpu-medusa) | other (stabilityai-ai-community) | none | - |
| stabilityai | [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | openrail++ | [LICENSE.md](data/licenses/stabilityai/stable-diffusion-xl-base-1.0.txt) | - |
| stepfun-ai | [GOT-OCR-2.0-hf](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf) | apache-2.0 | none | - |
| stepfun-ai | [GOT-OCR2_0](https://huggingface.co/stepfun-ai/GOT-OCR2_0) | apache-2.0 | none | - |
| stepfun-ai | [Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | apache-2.0 | none | - |
| stepfun-ai | [Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF) | apache-2.0 | none | - |
| stepfun-ai | [Step-5-Preview](https://huggingface.co/stepfun-ai/Step-5-Preview) | other | [LICENSE-CN.txt](data/licenses/stepfun-ai/Step-5-Preview.txt) | - |
| stepfun-ai | [Step-5-Preview-BF16](https://huggingface.co/stepfun-ai/Step-5-Preview-BF16) | other | [LICENSE-CN.txt](data/licenses/stepfun-ai/Step-5-Preview-BF16.txt) | - |
| stepfun-ai | [Step-5-Preview-NVFP4](https://huggingface.co/stepfun-ai/Step-5-Preview-NVFP4) | other (stepfun-model-license-1.0) | [LICENSE-CN.txt](data/licenses/stepfun-ai/Step-5-Preview-NVFP4.txt) | - |
| stepfun-ai | [step3](https://huggingface.co/stepfun-ai/step3) | apache-2.0 | [LICENSE](data/licenses/stepfun-ai/step3.txt) | - |
| tencent | [HunyuanOCR](https://huggingface.co/tencent/HunyuanOCR) | other (tencent-hunyuan-community) | [LICENSE](data/licenses/tencent/HunyuanOCR.txt) | - |
| tencent | [Hy-MT2-1.8B-GGUF](https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF) | apache-2.0 | [LICENSE.txt](data/licenses/tencent/Hy-MT2-1.8B-GGUF.txt) | - |
| tencent | [Hy-MT2-7B-GGUF](https://huggingface.co/tencent/Hy-MT2-7B-GGUF) | apache-2.0 | [LICENSE.txt](data/licenses/tencent/Hy-MT2-7B-GGUF.txt) | - |
| tencent | [Hy-Nomas-Diffusers](https://huggingface.co/tencent/Hy-Nomas-Diffusers) | apache-2.0 | [LICENSE](data/licenses/tencent/Hy-Nomas-Diffusers.txt) | - |
| tencent | [Hy-SimulMT-30B-A3B-Interleave-GGUF](https://huggingface.co/tencent/Hy-SimulMT-30B-A3B-Interleave-GGUF) | not set | [LICENSE.txt](data/licenses/tencent/Hy-SimulMT-30B-A3B-Interleave-GGUF.txt) | - |
| tencent | [Hy3](https://huggingface.co/tencent/Hy3) | apache-2.0 | [LICENSE](data/licenses/tencent/Hy3.txt) | - |
| tencent | [Qwen3.8-27B-DSpine-b16](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) | apache-2.0 | [LICENSE](data/licenses/tencent/Qwen3.8-27B-DSpine-b16.txt) | - |
| tencent | [WeVisOne-VL-2B](https://huggingface.co/tencent/WeVisOne-VL-2B) | apache-2.0 | [LICENSE](data/licenses/tencent/WeVisOne-VL-2B.txt) | - |
| tencent | [WeVisOne-VL-4B](https://huggingface.co/tencent/WeVisOne-VL-4B) | apache-2.0 | [LICENSE](data/licenses/tencent/WeVisOne-VL-4B.txt) | - |
| zai-org | [GLM-5](https://huggingface.co/zai-org/GLM-5) | mit | none | - |
| zai-org | [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | other (glm-5.3) | [LICENSE](data/licenses/zai-org/GLM-5.3.txt) | - |
| zai-org | [GLM-5.3-BF16](https://huggingface.co/zai-org/GLM-5.3-BF16) | other (glm-5.3) | [LICENSE](data/licenses/zai-org/GLM-5.3-BF16.txt) | - |
| zai-org | [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | mit | [LICENSE](data/licenses/zai-org/GLM-5.3-Flash.txt) | - |
| zai-org | [GLM-5.3-Flash-BF16](https://huggingface.co/zai-org/GLM-5.3-Flash-BF16) | mit | [LICENSE](data/licenses/zai-org/GLM-5.3-Flash-BF16.txt) | - |
| zai-org | [GLM-OCR](https://huggingface.co/zai-org/GLM-OCR) | mit | none | - |
<!-- table:end -->

## Notes

- License texts are copied as published by their owners and remain their property. Nothing here is legal advice; always read the original license on the model page.
- The code in this repository is MIT licensed. The collected data is published under CC BY 4.0.

A [GlobalFeed](https://globalfeed.ai) project, maintained by Şevki Özen.
