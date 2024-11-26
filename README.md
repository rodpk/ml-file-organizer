# ML File Organizer

The **ML File Organizer** is a machine learning-powered script that organizes your image files into categories based on their content. Using a pre-trained model, the application predicts the category of each image and automatically moves it into the corresponding folder.

---
## TODO
### First stage
- [ ] Setup logic to ignore non-image files
- [ ] Tune training to improve accuracy
- [x] Setup minimal accuracy before moving images
  - [x] If not confident enough, move it to a separate folder

### Second stage
- [ ] Create a GUI for easier use
  - [ ] User should be able to setup the respective folders
  - [ ] User should be able to train the model
  - [ ] User should be able to initialize organizing script
  - [ ] When predicting images:
    - [ ] Should not move instantly, instead should keep the state while wait for all the other images are predicted
    - [ ]  Should show a list to the user with each file with a checkmark to confirm wether to move or not
      - [ ]  Should show a small thumbnail so user can validate the image content

### Third stage
- [ ] Setup a unique pre-trained model so users can use
---

## Features
- Automatically organizes image files based on their predicted categories.
- Uses a pre-trained neural network for image classification (based on [FastAI](https://www.fast.ai/) and [PyTorch](https://pytorch.org/)).

---

## Requirements
- Python 3.9+
- Virtual environment (optional but recommended)
- Libraries listed in `requirements.txt`

---

## Setup Instructions

### 1. Setup environment
- Clone the repository
```bash
git clone https://github.com/your-username/ml-file-organizer.git
cd ml-file-organizer
```

- Setup the virtual environment (optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

- Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare environment variables
Create/Update the `settings.json` inside the `config` directory to configure the folders (make sure the projects has atleast rw access for the folders). 
```json
{
    "DATASET_PATH": "example/images",
    "TO_ORGANIZE_PATH": "example/to-organize",
    "MODEL_PATH": "models/image_organizer_model.pkl"
}
```


### 3. Train the model
In the initial steps of the application we dont have a properly trained model, so you have to train it using your own data.

```bash
python scripts/train_model.py
```

### 4. Run the organizer script OR setup watchdog
To run the organizer manually you can use: 
```bash
python scripts/predict_images.py
```

Or if you want the watchdog to keep listening to any events on the to-organize folder you can run:

```bash
python scripts/organize_watcher.py
```