from fastai.vision.all import *
from loguru import logger
import shutil
import os
import json

# read variables from configs.json
with open("config/settings.json", "r") as f:
    settings = json.load(f)


# paths
dataset_path = Path(settings["DATASET_PATH"])
to_organize_path = Path(settings["TO_ORGANIZE_PATH"])

# load model
learn = load_learner(settings["MODEL_PATH"])

confidence_treshold = 0.7 # minimum confidence
# predict and organize
for image_path in to_organize_path.iterdir():
    # predict category
    pred, pred_idx, probs = learn.predict(image_path)
    confidence = probs[pred_idx]
    
    logger.info(f"Predicted {image_path.name} to be in {pred}")
    logger.info(f"Confidence is {confidence:.2f}")
    
    if confidence >= confidence_treshold:
        # move to the predicted folder  
        target_folder = dataset_path / pred
        target_folder.mkdir(exist_ok=true)
        shutil.move(str(image_path), str(target_folder))
        logger.info(f"Moved {image_path.name} to {target_folder}")
    else:
        logger.info(f"Skipped {image_path.name} due to low confidence ({confidence:.2f})")

print("done with organizing")