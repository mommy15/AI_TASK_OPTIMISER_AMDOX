import speech_recognition as sr
from textblob import TextBlob
import io

def live_speech_emotion(audio_bytes):
    recognizer = sr.Recognizer()

    try:
        # Read WAV bytes directly (no conversion, no ffmpeg)
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        polarity = TextBlob(text).sentiment.polarity

        if polarity >= 0.6:
            emotion = "Happy"
        elif polarity > 0.3:
            emotion = "Positive"
        elif polarity < -0.3:
            emotion = "Stressed"
        else:
            emotion = "Neutral"

        return text, emotion, polarity

    except Exception:
        return "", "Neutral", 0.0

