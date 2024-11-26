import os
from fastai.vision.all import *

# Set up paths
data_path = Path("example/images")  # Path to training images
model_dir = Path("models")  # Directory for saving models

# Debug: Print contents to verify structure
print(f"Contents of {data_path}: {list(data_path.iterdir())}")

# Ensure the model directory exists
model_dir.mkdir(parents=True, exist_ok=True)

# Create DataLoaders
data = ImageDataLoaders.from_folder(
    data_path,
    train=".",  # Train on all organized folders
    valid_pct=0.2,  # 20% of data for validation
    item_tfms=Resize(224),  # Resize images to 224x224
    seed=42
)

# Debug: Show a sample batch
data.show_batch(max_n=9)

# Create the learner
learn = vision_learner(data, resnet34, metrics=error_rate)

# Set both the model directory and the learner path explicitly
learn.model_dir = model_dir
learn.path = Path(".")  # Set to the project root to avoid `example/images` base path

# Train the model
print("Starting training...")
learn.fine_tune(4)

# Save the model explicitly to the validated path
model_path = model_dir / "image_organizer_model.pkl"
learn.export(model_path)
print(f"Model saved to: {model_path}")
