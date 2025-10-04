import cv2
import numpy as np
from keras import models
import base64
import re

# Emotion dictionary
emotion_dict = {0: "Angry", 1: "Disgust", 2: "Anxious", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Relaxed"}

# Load model
with open('./emotion_model.json', 'r') as json_file:
    loaded_model_json = json_file.read()

emotion_model = models.model_from_json(loaded_model_json)
emotion_model.load_weights('./emotion_model.weights.h5')
print("Emotion model loaded successfully!")

def predict_emotion_from_base64(img_base64):
    """
    Takes a base64-encoded image string from the browser, detects the first face, 
    and predicts the emotion. Returns the emotion index or None if no face detected.
    """
    # Remove prefix if present
    img_str = re.sub('^data:image/.+;base64,', '', img_base64)
    img_bytes = base64.b64decode(img_str)

    # Convert bytes to numpy array
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        return None  # No face detected

    x, y, w, h = faces[0]  # Use first detected face
    roi_gray = gray[y:y+h, x:x+w]
    cropped_img = cv2.resize(roi_gray, (48, 48))
    cropped_img = np.expand_dims(np.expand_dims(cropped_img, -1), 0)

    prediction = emotion_model.predict(cropped_img, verbose=0)
    max_index = int(np.argmax(prediction))
    return max_index
