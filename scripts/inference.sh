#!/usr/bin/bash

INPUT_FOLDER='/media/storage/luu/nnUNet_raw/Dataset222_SBT/imagesTs'
OUTPUT_FOLDER='/media/storage/luu/nnUNet_predictions/Dataset222_SBT/nnUNetTrainerSegResNet__nnUNetPlans__3d_fullres/fold_0'
nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d 111 -c 3d_fullres -f 0 -tr nnUNetTrainerSegResNet -chk checkpoint_best.pth --disable_progress_bar
