from fastai.vision.all import *
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

# predict and organize
for image_path in to_organize_path.iterdir():
    # predict category
    pred, pred_idx, probs = learn.predict(image_path)
    
    # move to the predicted folder
    target_folder = dataset_path / pred
    target_folder.mkdir(exist_ok=true)
    shutil.move(str(image_path), str(target_folder))
    print(f"Moved {image_path.name} to {target_folder}")

print("done with organizing")