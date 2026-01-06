from deepface import DeepFace
import cv2

def video_emotion(frame):
    try:
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )
        emotion = result[0]['dominant_emotion']
        return emotion
    except:
        return "Neutral"
