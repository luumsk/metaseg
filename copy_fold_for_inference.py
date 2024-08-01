import json
import os
import glob
import shutil

FOLD_IDX = 4

with open('/media/storage/suvorov/nnUNet_preprocessed/Dataset001_META/splits_final.json') as fp:
    samples = json.load(fp)[FOLD_IDX]['val']

for sample in samples:
    sample_channels = glob.glob(f'/media/storage/suvorov/nnUNet_raw/Dataset001_META/imagesTr/{sample}_*.nii.gz')
    for ch in sample_channels:
        shutil.copyfile(ch, f'/home/suvorov/meta_nnunet/inference_input/{os.path.basename(ch)}')
