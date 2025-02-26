# src/image_analysis.py
import cv2  # Example library for image processing
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('../models/image_model.h5')

def analyze_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Perform some analysis (this is just a placeholder)
    if image is None:
        return "Image not found."
    
    # Preprocess the image for the model
    image = cv2.resize(image, (224, 224))  # Resize to match model input
    image = image / 255.0  # Rescale pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Make a prediction
    prediction = model.predict(image)
    
    # Interpret the prediction
    if prediction[0] > 0.5:
        return "Image is likely tampered."
    else:
        return "Image is likely original."