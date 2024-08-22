# Metastases Segmentation

Before running the code, go to this file `U-Mamba/umamba/nnunetv2/paths.py` and change `line 46-48` to:

```python
nnUNet_raw = os.environ.get('nnUNet_raw')
nnUNet_preprocessed = os.environ.get('nnUNet_preprocessed')
nnUNet_results = os.environ.get('nnUNet_results')
```

Then change the directories to yours in this file `scripts/setvars.sh` and run it to set up paths.

```bash
export nnUNet_raw=<YOUR_PATH>
export nnUNet_preprocessed=<YOUR_PATH>
export nnUNet_results=<YOUR_PATH>
```

