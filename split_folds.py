import os
import json
import numpy as np
from sklearn.model_selection import KFold

# Load filenames
fns = os.listdir('/media/storage/luu/nnUNet_raw/Dataset111_Meta/imagesTr')
print(f'Number of training filenames: {len(fns)}')

# Extract unique patient IDs from filenames
patients = sorted(list(set(fn[:15] for fn in fns)))  # Ensure patients are sorted
patients = np.array(patients)
print(f'Number of unique patients: {len(patients)}')
print('')

# Set up KFold with shuffling
kf = KFold(n_splits=5, shuffle=True, random_state=12345)
splits = []

for i, (train_index, val_index) in enumerate(kf.split(patients)):
    train_patients = patients[train_index]
    val_patients = patients[val_index]
    print(f'Fold {i}: {len(train_patients)} train patients, {len(val_patients)} val patients')

    # Get and sort train filenames for the current fold
    train_fns_fold = sorted(list(set([fn[:19] for fn in fns if fn[:15] in train_patients])))
    print(f'{len(train_fns_fold)} train files')

    # Get and sort val filenames for the current fold
    val_fns_fold = sorted(list(set([fn[:19] for fn in fns if fn[:15] in val_patients])))
    print(f'{len(val_fns_fold)} val files')
    print('')

    splits.append({'train': train_fns_fold, 'val': val_fns_fold})
 
# Save splits with sorted keys
with open('splits_final.json', 'w') as f:
    json.dump(splits, f, sort_keys=True, indent=4)

# Test for duplicated patients in train and val sets
print('Test duplicated patients in train and val sets')
for i, fold in enumerate(splits):
    train_patients = set(fn[:-4] for fn in fold['train'])
    val_patients = set(fn[:-4] for fn in fold['val'])
    intersection = train_patients & val_patients
    print(f"Fold {i}: {intersection or 'clean'}")
