DATA_DIR="/media/storage/hdd_bair/BraTS24/MICCAI-BraTS2024-MET-Challenge-TrainingData"

NNUNET_IMGS_DIR="/media/storage/suvorov/nnUNet_raw/Dataset003_META24/imagesTr"
NNUNET_LBLS_DIR="/media/storage/suvorov/nnUNet_raw/Dataset003_META24/labelsTr"
mkdir -p $NNUNET_IMGS_DIR
mkdir -p $NNUNET_LBLS_DIR

for SAMPLE in ${DATA_DIR}/*
do
    SAMPLE_IDX=$(basename "$SAMPLE" | cut -d '-' -f 3)
    echo "Copying training sample #${SAMPLE_IDX}"

    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t1c.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0000.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t1n.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0001.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t2f.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0002.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t2w.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0003.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-seg.nii.gz" "${NNUNET_LBLS_DIR}/META24_${SAMPLE_IDX}.nii.gz"
done
