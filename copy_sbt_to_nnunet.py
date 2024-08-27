import os
import json
import shutil

def get_subdirectories(directory):
    """Return a list of subdirectories in the given directory."""
    return [subdir for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]

def check_missing_modalities(subdir_path, file_mapping):
    """Check for missing modalities in the given subdirectory."""
    missing_modalities = []
    for modality, pattern in file_mapping.items():
        if not any(pattern in filename for filename in os.listdir(subdir_path)):
            missing_modalities.append(modality)
    return missing_modalities

def collect_file_paths(subdir_path, file_mapping):
    """Collect file paths that match the required modalities in the subdirectory."""
    file_paths = {}
    for modality, pattern in file_mapping.items():
        for filename in os.listdir(subdir_path):
            if pattern in filename:
                file_paths[modality] = os.path.join(subdir_path, filename)
                break
    return file_paths

def generate_new_file_paths(id_, new_data_dir, new_label_dir):
    """Generate new file paths for the nnUNet format."""
    new_id = f"SBT-MET-{id_.replace('_', '-')}"
    return {
        'seg': os.path.join(new_label_dir, f'{new_id}.nii.gz'),
        't1c': os.path.join(new_data_dir, f'{new_id}_0000.nii.gz'),
        't1n': os.path.join(new_data_dir, f'{new_id}_0001.nii.gz'),
        't2f': os.path.join(new_data_dir, f'{new_id}_0002.nii.gz'),
        't2w': os.path.join(new_data_dir, f'{new_id}_0003.nii.gz'),
    }

def copy_files(original_fps_dict, nnunet_fps_dict):
    """Copy files from the original paths to the new nnUNet paths."""
    for id_, original_paths in original_fps_dict.items():
        for modality, original_path in original_paths.items():
            if id_ in nnunet_fps_dict:
                nnunet_path = nnunet_fps_dict[id_][modality]
                shutil.copyfile(original_path, nnunet_path)
                print(f"Copied {original_path} to {nnunet_path}")

def main():
    # SBT for training
    # data_dir = '/media/storage1/groza/data/210312'
    # new_data_dir = '/media/storage1/luu/nnUNet_raw/Dataset222_SBT/imagesTr'
    # new_label_dir = '/media/storage1/luu/nnUNet_raw/Dataset222_SBT/labelsTr'

    # SBT for validation
    data_dir = '/media/storage1/groza/data/210618'
    new_data_dir = '/media/storage1/luu/nnUNet_raw/Dataset222_SBT/imagesTs'
    new_label_dir = '/media/storage1/luu/nnUNet_raw/Dataset222_SBT/labelsTs'

    file_mapping = {
        'seg': 'Segmentation1-label.nii.gz',
        't1n': 'reg_t1.nii.gz',
        't1c': 'reg_t1c.nii.gz',
        't2w': 'reg_t2_tra.nii.gz',
        't2f': 'reg_t2f.nii.gz'
    }

    original_fps_dict = {}
    subdirs = get_subdirectories(data_dir)
    
    print(f"Checking {len(subdirs)} IDs for missing modalities...")

    # Check each subdirectory for missing modalities and collect file paths
    for subdir in subdirs:
        subdir_path = os.path.join(data_dir, subdir)
        missing_modalities = check_missing_modalities(subdir_path, file_mapping)
        
        if missing_modalities:
            print(f"ID: {subdir} is missing the following modalities: {', '.join(missing_modalities)}")
        else:
            file_paths = collect_file_paths(subdir_path, file_mapping)
            if len(file_paths) == len(file_mapping):
                original_fps_dict[subdir] = file_paths

    # Generate and save the new file paths for nnUNet
    nnunet_fps_dict = {}
    for id_, paths in original_fps_dict.items():
        nnunet_fps_dict[id_] = generate_new_file_paths(id_, new_data_dir, new_label_dir)

    # Save paths dict to JSON files
    # with open('sbt_train.json', 'w') as f:
    #     json.dump(original_fps_dict, f, indent=4)
    # print("Saved original file paths dict to 'sbt_train.json'.")

    # with open('sbt_nnUnet_train.json', 'w') as f:
    #     json.dump(nnunet_fps_dict, f, indent=4)
    # print("Saved nnunet file paths dict to 'sbt_nnUnet_train.json'.")

    # Copy the files from original paths to nnUNet paths
    copy_files(original_fps_dict, nnunet_fps_dict)

if __name__ == "__main__":
    main()
