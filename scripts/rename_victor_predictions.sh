#!/usr/bin/bash

pred_dir="/media/storage/suvorov/nnUNet_raw/Dataset003_META24/labelsTs_Tversky"
pred_fns=($(ls $pred_dir/*.nii.gz))

echo "Number of prediction files: ${#pred_fns[@]}"

for fn in "${pred_fns[@]}"; do
    base_fn=$(basename "$fn")
    new_fn=$(echo "$base_fn" | sed -e 's/META24_/BraTS-MET-/' -e 's/\.nii\.gz/-000.nii.gz/')
    new_fp="$pred_dir/$new_fn"
    cp "$fn" "$new_fp"
done
