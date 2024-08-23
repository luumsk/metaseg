import json


splits = None
with open('splits_final.json', 'r') as f:
    splits = json.load(f)

# Test for duplicated patients in train and val sets
print('Test duplicated patients in train and val sets')
for i, fold in enumerate(splits):
    train_patients = set(fn[:-4] for fn in fold['train'])
    val_patients = set(fn[:-4] for fn in fold['val'])
    intersection = train_patients & val_patients
    print(f"Fold {i}: {intersection or 'clean'}")
