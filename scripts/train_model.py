import os
import shutil
from fastai.vision.all import *

dataset_path = Path("/example/images")
to_organize_path = Path("/example/to-organize")

data = ImageDataLoaders.from_folder(
    dataset_path,
    train=".", # train on all organized folders
    valid_pct=0.2, # 20% of data for validation
    item_tfms=Resize(224), # resize images to 224x224
    seed=42
)

# create and train model
learn = vision_learner(data, resnet18, metrics=accuracy)
learn.fine_tune(4) # train for 4 epochs

# save model
learn.export("image_organizer_model.pkl")