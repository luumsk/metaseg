#!/usr/bin/bash

INPUT_FOLDER='/media/storage/luu/nnUNet_raw/Dataset999_Metastases/imagesTs'

# UmambaBot 3d all (reorient)
# OUTPUT_FOLDER='/media/storage/luu/nnUNet_predictions/Dataset999_Metastases/fold_all'
# nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d 999 -c 3d_fullres -f all -tr nnUNetTrainerUMambaBot -chk checkpoint_best.pth --disable_progress_bar

# UmambaBot 3d fold 1 (reorient)
# OUTPUT_FOLDER='/media/storage/luu/nnUNet_predictions/Dataset999_Metastases/fold_1'
# nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d 999 -c 3d_fullres -f 1 -tr nnUNetTrainerUMambaBot -chk checkpoint_best.pth --disable_progress_bar

# UmambaBot 3d fold 0 
# OUTPUT_FOLDER='/media/storage/luu/nnUNet_predictions/Dataset111_Meta/fold_0'
# nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d 111 -c 3d_fullres -f 0 -tr nnUNetTrainerUMambaBot -chk checkpoint_best.pth --disable_progress_bar

# SegResNet 3d fold 0 
# OUTPUT_FOLDER='/media/storage/luu/nnUNet_predictions/Dataset111_Meta/nnUNetTrainerSegResNet__nnUNetPlans__3d_fullres/fold_0'
# nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d 111 -c 3d_fullres -f 0 -tr nnUNetTrainerSegResNet -chk checkpoint_best.pth --disable_progress_bar

# UNetR 3d fold 0 
# OUTPUT_FOLDER='/media/storage/luu/nnUNet_predictions/Dataset111_Meta/nnUNetTrainerUNETR__nnUNetPlans__3d_fullres/fold_0'
# nnUNetv2_predict -i $INPUT_FOLDER -o $OUTPUT_FOLDER -d 111 -c 3d_fullres -f 0 -tr nnUNetTrainerUNETR -chk checkpoint_best.pth --disable_progress_bar