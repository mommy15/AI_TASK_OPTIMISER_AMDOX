from deepface import DeepFace

def video_emotion(frame):
    """
    Detect dominant facial emotion from a video frame.
    This function is cloud-safe because it does NOT import cv2.
    """
    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        return result[0]["dominant_emotion"]

    except Exception:
        return "Neutral"
