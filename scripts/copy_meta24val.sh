DATA_DIR="/media/storage/hdd_bair/BraTS24/MICCAI-BraTS2024-MET-Challenge-Validation"

NNUNET_IMGS_DIR="/media/storage/suvorov/nnUNet_raw/Dataset003_META24/imagesTs"
mkdir -p $NNUNET_IMGS_DIR

for SAMPLE in ${DATA_DIR}/*
do
    SAMPLE_IDX=$(basename "$SAMPLE" | cut -d '-' -f 3)
    echo "Copying validation sample #${SAMPLE_IDX}"

    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t1c.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0000.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t1n.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0001.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t2f.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0002.nii.gz"
    cp "${SAMPLE}/BraTS-MET-${SAMPLE_IDX}-000-t2w.nii.gz" "${NNUNET_IMGS_DIR}/META24_${SAMPLE_IDX}_0003.nii.gz"
done
