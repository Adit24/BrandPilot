import cv2
import numpy as np
from PIL import Image
from io import BytesIO


def compare_logo(reference_bytes, creative_bytes):
    reference = Image.open(BytesIO(reference_bytes)).convert("RGB")
    creative = Image.open(BytesIO(creative_bytes)).convert("RGB")

    reference_img = cv2.cvtColor(np.array(reference), cv2.COLOR_RGB2GRAY)
    creative_img = cv2.cvtColor(np.array(creative), cv2.COLOR_RGB2GRAY)

    orb = cv2.ORB_create(nfeatures=1500)

    keypoints_ref, descriptors_ref = orb.detectAndCompute(reference_img, None)
    keypoints_creative, descriptors_creative = orb.detectAndCompute(
        creative_img, None
    )

    if descriptors_ref is None or descriptors_creative is None:
        return {
            "score": 0,
            "matches": 0,
            "reference_features": len(keypoints_ref),
            "creative_features": len(keypoints_creative),
            "status": "Insufficient visual features for comparison."
        }

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    pairs = matcher.knnMatch(descriptors_ref, descriptors_creative, k=2)

    good_matches = [
        first for first, second in pairs
        if first.distance < 0.75 * second.distance
    ]

    score = round(
        100 * len(good_matches) / max(len(keypoints_ref), 1), 2
    )

    if len(good_matches) >= 15 and score >= 15:
        status = "Potential logo match detected. Human verification required."
    else:
        status = "Weak logo match. Review the creative manually."

    return {
        "score": score,
        "matches": len(good_matches),
        "reference_features": len(keypoints_ref),
        "creative_features": len(keypoints_creative),
        "status": status
    }