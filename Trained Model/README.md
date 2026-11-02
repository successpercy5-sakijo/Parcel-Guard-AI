BOX DAMAGE DETECTOR

WHAT IS IN THIS FOLDER
- AI_Damage_Detector.ipynb              Training notebook (baseline CNN, then final MobileNetV2 transfer-learning model)
- box_damage_classifier_mobilenet.keras Final trained model used by the app (MobileNetV2, 160x160, sigmoid output)
- main.py                               Streamlit app (upload a photo or use the camera)
- requirements.txt                      Python packages needed
- optional_baseline_model/              The first small CNN (64x64), kept for comparison
- Report                                Add your exported report (Word or PDF) to this folder before sending.
- training_data/                        Add your image dataset here if the assignment requires it.

HOW TO RUN THE APP
1. Install Python 3.10 or newer.
2. Open a terminal in this folder and run:   pip install -r requirements.txt
3. Start the app:                           streamlit run main.py
   (main.py must stay in the same folder as box_damage_classifier_mobilenet.keras)

MODEL SUMMARY
- Task: binary image classification (damaged = 0, intact = 1)
- Final model: frozen MobileNetV2 (ImageNet weights) + GlobalAveragePooling + Dense(128, ReLU) + Dropout(0.5) + Dense(1, sigmoid)
- Training: Adam, binary cross-entropy, augmentation (shear, zoom, flip), early stopping
- Data: 349 training, 100 validation, 27 test images
- Results: about 91% best validation accuracy, 100% test accuracy (small test set); baseline CNN scored 51.85% on the test set

HOW TO RUN THE NOTEBOOK
Place the training_data folder (trainning / validating / testing, each with damaged and intact subfolders) next to the notebook, then run the cells in order.
