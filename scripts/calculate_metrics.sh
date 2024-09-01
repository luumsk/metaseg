#!/usr/bin/bash
PR='/media/storage/luu/nnUNet_predictions/Dataset222_SBT/nnUNetTrainerSegResNet__nnUNetPlans__3d_fullres/fold_0'
GT='/media/storage/luu/nnUNet_raw/Dataset222_SBT/labelsTs'
python meta24_compute_metrics.py --pr $PR --gt $GT