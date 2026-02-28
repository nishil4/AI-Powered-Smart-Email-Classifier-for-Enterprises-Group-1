# AI-Powered-Smart-Email-Classifier-for-Enterprises-Group-1

This repository contains a Jupyter notebook (`module1.ipynb`) demonstrating email classification preprocessing and training workflows.

---

## Setup & Dataset Access

The dataset used in the notebook is hosted on Hugging Face and is **gated**. To load it successfully you must authenticate:

1. **Obtain a Hugging Face access token** from https://huggingface.co/settings/tokens
2. **Set an environment variable** before running the notebook:
   ```bash
   export HUGGINGFACE_HUB_TOKEN="<your_token_here>"  # or HF_TOKEN
   ```
   Alternatively, install the `huggingface_hub` package and run one of the
   following in a shell (use the same Python environment as the notebook):
   ```bash
   pip install huggingface_hub  # if not already installed
   hf login                    # the CLI executable is now named `hf`
   # or, if the CLI still isn't found:
   python -m huggingface_hub login
   # or explicitly:
   python -m huggingface_hub.cli.hf login
   ```
   You can also authenticate programmatically inside the notebook:
   ```python
   from huggingface_hub import login
   login(token="<your_token_here>")
   ```
4. Re-run the dataset loading cell in `module1.ipynb`. The code now detects
   the token and passes it to `load_dataset`.

Without authentication the notebook will print an error message explaining
the requirement.

---
