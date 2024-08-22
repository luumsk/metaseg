# Metastases Segmentation

### Set environment variables
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

### Split folds

The default nnUnet split fold function consider patient with different timestamps different files and therefore, may split them into train and val sets. To avoid data leakage, we use the manual spliting. To create `split_final.json`, run `python splilt_folds.py`