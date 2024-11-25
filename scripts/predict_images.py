from fastai.vision.all import *
import shutil
import os

# paths
dataset_path = Path("/example/images")
to_organize_path = Path("/example/to-organize")

# load model
learn = load_learner("/models/image_organizer_model.pkl")

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