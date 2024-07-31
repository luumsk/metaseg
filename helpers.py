import os, json
import nibabel as nib
import SimpleITK as sitk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from celluloid import Camera
from IPython.display import HTML


def get_nifti_details_for_one_file(filepath):
    # Load image object
    img = nib.load(filepath)
    header = img.header

    # Shape
    shape = header.get_data_shape()

    # Spacing
    spacing = header.get_zooms()

    # Orientation
    orientation = nib.orientations.aff2axcodes(img.affine)

    # Affine
    affine = img.affine.copy()

    # Intensity
    try:
        image_data = img.get_fdata()
    except:
        print(f'Error when run .get_dfata() for this image using Nibabel: {filepath}')
        print('Using SimpleITK')
        img = sitk.ReadImage(filepath)
        image_data = sitk.GetArrayFromImage(img)
    
    intensity = (image_data.min(), image_data.max())

    return {
        'filepath'   : filepath,
        'shape'      : shape,
        'orientation': orientation,
        'spacing'    : spacing,
        'affine'     : affine,
        'intensity'  : intensity
    }

def get_nifti_details(file_dict):
    nifti_details_list = []

    for paths in file_dict.values():
        for path in paths:
            nifti_details_list.append(get_nifti_details_for_one_file(path))
    
    return nifti_details_list