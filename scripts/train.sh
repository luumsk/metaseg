#!/usr/bin/bash

# nnUNetTrainerSegResNet
CUDA_VISIBLE_DEVICES=0 nnUNetv2_train 111 3d_fullres 0 -tr nnUNetTrainerSegResNet
