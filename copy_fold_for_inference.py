import json
import os
import glob
import shutil

FOLD_IDX = 4

with open('/media/storage/luu/nnUNet_preprocessed/Dataset111_Meta/splits_final.json') as fp:
    samples = json.load(fp)[FOLD_IDX]['val']

for sample in samples:
    sample_channels = glob.glob(f'/media/storage/luu/nnUNet_raw/Dataset111_Meta/imagesTr/{sample}_*.nii.gz')
    for ch in sample_channels:
        shutil.copyfile(ch, f'/home/luu/metaseg/inference_input/{os.path.basename(ch)}')
