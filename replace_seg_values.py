import os
import nibabel as nib
import numpy as np

def replace_values(data, mapping):
    """Replace values in the NIfTI data according to the given mapping."""
    new_data = np.copy(data)
    for old_value, new_value in mapping.items():
        new_data[data == old_value] = new_value
    return new_data

def process_nii_file(filepath, mapping):
    """Load a NIfTI file, replace values according to mapping, and save the result."""
    # Load the NIfTI file
    img = nib.load(filepath)
    data = img.get_fdata()

    # Replace values according to the mapping
    new_data = replace_values(data, mapping)

    # Create a new NIfTI image with the modified data
    new_img = nib.Nifti1Image(new_data, img.affine, img.header)

    # Save the modified NIfTI file
    nib.save(new_img, filepath)
    print(f"Processed file: {filepath}")

def main(directory):
    # Define the mapping from SBT to BraTS values
    mapping = {
        # SBT -> BraTS
        1: 1,
        2: 3,
        3: 2,
        4: 2,
    }

    # Process each NIfTI file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".nii.gz"):
            filepath = os.path.join(directory, filename)
            process_nii_file(filepath, mapping)

if __name__ == "__main__":
    directory = "/media/storage1/luu/nnUNet_raw/Dataset222_SBT/labelsTr"
    main(directory)
