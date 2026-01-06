import streamlit as st
import pandas as pd
import uuid
from datetime import datetime
import cv2
import os


from emotion_speech_live import live_speech_emotion
from emotion_text import text_emotion
from emotion_video import video_emotion
from task_logic import recommend_tasks, stress_alert

st.set_page_config(page_title="AI Task Optimizer", layout="wide")
st.title("AI-Powered Task Optimizer")

MENU = st.sidebar.selectbox(
    "Select Mode",
    ["Text Emotion", "Speech Emotion", "Video Emotion", "Analytics"]
)

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "mood_logs.csv")

def log_emotion(mode, emotion, confidence=None):
    os.makedirs(DATA_DIR, exist_ok=True)

    # Create file if not exists
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=[
            "employee_id",
            "mode",
            "emotion",
            "confidence",
            "timestamp"
        ])
        df.to_csv(DATA_FILE, index=False)

    # Append new row
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = [
        str(uuid.uuid4())[:6],
        mode,
        emotion,
        confidence,
        datetime.now()
    ]
    df.to_csv(DATA_FILE, index=False)

# TEXT - Emotion Analysis
if MENU == "Text Emotion":
    text = st.text_area("How are you feeling today?")

    if st.button("Analyze Text"):
        emotion, score = text_emotion(text)
        st.success(f"Emotion: {emotion}")
        log_emotion(
        mode="text",
        emotion=emotion,
        confidence=round(score, 2)
    )
        tasks = recommend_tasks(emotion)
        st.write("### Recommended Tasks")
        for t in tasks:
            st.write("•", t)

        if stress_alert(emotion):
            st.warning("⚠ HR Alert: Stress detected")

# SPEECH - Emotion Analysis
elif MENU == "Speech Emotion":
    st.subheader(" Live Speech Emotion Detection")

    # Streamlit native audio recorder (NO ffmpeg needed)
    audio_file = st.audio_input("Record your voice")

    if audio_file is not None:
        audio_bytes = audio_file.getvalue()

        # Playback
        st.audio(audio_bytes, format="audio/wav")

        if st.button("Analyze Speech"):
            text, emotion, score = live_speech_emotion(audio_bytes)

            if text.strip() == "":
                st.warning("⚠ Could not recognize speech clearly. Please try again.")
            else:

                log_emotion(
                mode="speech",
                emotion=emotion,
                confidence=round(score, 2)
                )
                st.write("🗣 **Recognized Text:**", text)
                st.success(f"Detected Emotion: **{emotion}**")
                st.info(f"Sentiment Score: {round(score, 2)}")

                # HR alert
                if stress_alert(emotion):
                    st.warning("⚠ HR Alert: Prolonged stress detected")

                # Task recommendation
                st.write("### Recommended Tasks")
                for task in recommend_tasks(emotion):
                    st.write("•", task)

 

# VIDEO - Emotion Analysis
elif MENU == "Video Emotion":
    st.subheader(" Live Video Emotion Detection")
    st.info("Start the camera to detect facial emotion in real time")

    run = st.checkbox("Start Camera")

    FRAME_WINDOW = st.image([])
    emotion_display = st.empty()

    if run:
        cam = cv2.VideoCapture(0)
        frame_count = 0
        detected_emotion = "Neutral"

        while run:
            ret, frame = cam.read()
            if not ret:
                st.error(" Unable to access webcam")
                break

            # Run emotion detection every 15 frames (performance boost)
            if frame_count % 30 == 0:
                log_emotion(
                mode="video",
                emotion=detected_emotion,
                confidence=None
            )
                detected_emotion = video_emotion(frame)

            frame_count += 1

            # Overlay emotion on frame
            cv2.putText(
                frame,
                detected_emotion,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            FRAME_WINDOW.image(frame, channels="BGR")
            emotion_display.markdown(f"### Detected Emotion: **{detected_emotion}**")

        cam.release()
    else:
        st.warning("Camera is off")


#  ANALYTICS - Emotion Logs
elif MENU == "Analytics":
    df = pd.read_csv(DATA_FILE)
    st.write("Logged Records:", len(df))
    st.dataframe(df)

