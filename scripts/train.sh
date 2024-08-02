#!/usr/bin/bash

# nnUNetTrainerUMambaBot
# nnUNetv2_train 111 3d_fullres 0 -tr nnUNetTrainerUMambaBot

# nnUNetTrainerSwinUNETR
# nnUNetv2_train 111 3d_fullres 0 -tr nnUNetTrainerSwinUNETR

# nnUNetTrainerSegResNet
CUDA_VISIBLE_DEVICES=0 nnUNetv2_train 111 3d_fullres 0 -tr nnUNetTrainerSegResNet

# nnUNetTrainerUNETR
# nnUNetv2_train 111 3d_fullres 0 -tr nnUNetTrainerUNETR
# CHECKPOINT='/media/storage/luu/nnUNet_results/Dataset111_Meta/nnUNetTrainerUNETR__nnUNetPlans__3d_fullres/fold_0'
# nnUNetv2_train 111 3d_fullres 0 -tr nnUNetTrainerUNETR --c

# nnUNet default
# nnUNetv2_train 111 3d_fullres 0

# CUDA_VISIBLE_DEVICES=1 nnUNetv2_train 111 3d_fullres 1 [--npz] &\
# CUDA_VISIBLE_DEVICES=2 nnUNetv2_train 111 3d_fullres 2 [--npz] &\
# CUDA_VISIBLE_DEVICES=3 nnUNetv2_train 111 3d_fullres 3 [--npz] &\