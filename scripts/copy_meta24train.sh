DATA_DIR="/media/storage1/BraTS24/MICCAI-BraTS2024-MET-Challenge-TrainingData"

NNUNET_IMGS_DIR="/media/storage1/luu/nnUNet_raw/Dataset111_Meta/imagesTr"
NNUNET_LBLS_DIR="/media/storage1/luu/nnUNet_raw/Dataset111_Meta/labelsTr"
mkdir -p $NNUNET_IMGS_DIR
mkdir -p $NNUNET_LBLS_DIR

for SAMPLE_PTH in ${DATA_DIR}/*
do
    SAMPLE_ID=$(basename "$SAMPLE_PTH")
    echo "Copying training sample ${SAMPLE_ID}"

    cp "${SAMPLE_PTH}/${SAMPLE_ID}-t1c.nii.gz" "${NNUNET_IMGS_DIR}/${SAMPLE_ID}_0000.nii.gz"
    cp "${SAMPLE_PTH}/${SAMPLE_ID}-t1n.nii.gz" "${NNUNET_IMGS_DIR}/${SAMPLE_ID}_0001.nii.gz"
    cp "${SAMPLE_PTH}/${SAMPLE_ID}-t2f.nii.gz" "${NNUNET_IMGS_DIR}/${SAMPLE_ID}_0002.nii.gz"
    cp "${SAMPLE_PTH}/${SAMPLE_ID}-t2w.nii.gz" "${NNUNET_IMGS_DIR}/${SAMPLE_ID}_0003.nii.gz"
    cp "${SAMPLE_PTH}/${SAMPLE_ID}-seg.nii.gz" "${NNUNET_LBLS_DIR}/${SAMPLE_ID}.nii.gz"
done
