
#  AI Task Optimiser - Data Science (AMDOX Internship Project)

An **AI-powered Streamlit application** that analyzes employee emotions using **text, live speech, and webcam video** to recommend suitable tasks, detect stress, and log emotional trends for analytics.

This project was developed as part of an **internship-level Data Science / AI project** with a focus on **real-time emotion analysis, productivity optimization, and ethical data handling**.

---

##  Features

###  1. Text Emotion Analysis

* Employees enter free-form text describing their feelings
* Sentiment analysis using **TextBlob**
* Emotions classified as:

  * Happy
  * Positive
  * Neutral
  * Stressed

---

###  2. Live Speech Emotion Detection

* Uses **Streamlit’s native `st.audio_input`**
* Converts speech → text using **SpeechRecognition**
* Emotion inferred from sentiment polarity
* No external tools like FFmpeg or PyAudio required

---

###  3. Live Video (Webcam) Emotion Detection

* Real-time webcam feed using **OpenCV**
* Facial emotion recognition using **DeepFace**
* Emotion detected periodically (optimized for performance)
* No video frames stored (privacy-first design)

---

###  4. Task Recommendation Engine

* Recommends tasks based on detected emotion:

  * High-focus tasks for positive/happy emotions
  * Routine tasks for neutral states
  * Light tasks & breaks for stressed emotions

---

###  5. Stress Detection & Alerts

* Detects stress-related emotions (`sad`, `angry`, `fear`, `stressed`)
* Displays HR alert warnings inside the UI

---

###  6. Emotion Data Logging

* Logs anonymized records into CSV
* Stored fields:

  * Employee ID (UUID-based, anonymous)
  * Mode (text / speech / video)
  * Emotion
  * Confidence score (where applicable)
  * Timestamp

---

###  7. Analytics & History

* View all logged emotion records
* Supports team-level mood analytics and trend tracking

---

##  Project Structure

```
AI_TASK_OPTIMISER_AMDOX/
│
├── app.py                     # Main Streamlit application
├── emotion_text.py            # Text emotion detection logic
├── emotion_speech_live.py     # Live speech emotion detection
├── emotion_video.py           # Webcam facial emotion detection
├── task_logic.py              # Task recommendation & stress logic
│
├── data/
│   └── mood_logs.csv          # Logged emotion data (CSV)
│
├── requirements.txt           # Project dependencies
├── runtime.txt
├── LICENSE                    # MIT License
├── .gitignore
```

---

##  Tech Stack

| Category        | Technology            |
| --------------- | --------------------- |
| Frontend        | Streamlit             |
| NLP             | TextBlob              |
| Speech-to-Text  | SpeechRecognition     |
| Computer Vision | OpenCV                |
| Facial Emotion  | DeepFace              |
| ML Backend      | TensorFlow / tf-keras |
| Data Storage    | CSV (Pandas)          |

---

##  Installation & Setup

###  1. Clone the Repository

```bash
git clone https://github.com/mommy15/AI_TASK_OPTIMISER_AMDOX.git
cd AI_TASK_OPTIMISER_AMDOX
```

---

###  2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

###  3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  4. Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

---

###  5. Run the Application

```bash
streamlit run app.py
```

---

##  Notes on Audio & Video

* **Speech input** uses `st.audio_input` (Streamlit native)
* No FFmpeg, PyAudio, or external system tools required
* Webcam access requires:

  * No other app (Zoom, Teams) using the camera
  * Camera permission enabled

##  Deployment

The application is deployed on **Streamlit Cloud** for easy access and demonstration.

**Live App:** <[ai-task-optimiser.streamlit.app](https://ai-task-optimiser.streamlit.app)>

### ⚠ Important Deployment Note
- Text emotion analysis and live speech emotion detection work fully on Streamlit Cloud.
- Webcam-based facial emotion detection is **disabled in the cloud environment** due to browser and server security limitations.
- Video emotion detection works **only when the application is run locally**.

This behavior is expected and handled gracefully in the application.


---

##  Data Privacy & Ethics

* No personal identifiers stored
* No raw audio or video data saved
* Only derived emotion labels are logged
* Employee IDs are anonymized using UUIDs

This project follows a **privacy-by-design approach**.

---

##  Example Logged Data

```csv
employee_id,mode,emotion,confidence,timestamp
a91c3f,speech,Happy,0.67,2026-01-06 10:22:41
```

---

##  Future Enhancements

* Multimodal emotion fusion (text + speech + video combined)
* Burnout prediction using time-series analysis
* Role-based dashboards for HR and managers
* Database integration (MongoDB / PostgreSQL)
* Email or Slack notifications for stress alerts
* Cloud deployment (Streamlit Cloud / AWS)

---

##  License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.

---

##  Author

** Medidha Michael David**
Data Science / Data Analytics Intern
GitHub: [https://github.com/mommy15](https://github.com/mommy15)

---

##  Acknowledgements

* Streamlit
* TextBlob
* SpeechRecognition
* DeepFace
* TensorFlow

---

