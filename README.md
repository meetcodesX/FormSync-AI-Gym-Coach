# FormSync --- AI Gym Coach

> Real-time AI gym coach using computer vision, pose detection, rep
> counting, form analysis, and AI voice feedback.

## 🚀 Overview

**FormSync** turns your camera into an intelligent workout assistant.

It uses real-time pose detection to analyze exercise movements, count
repetitions, track sets, detect common form issues, and provide
AI-powered coaching feedback through voice.

## ✨ Features

-   🎥 Real-time camera-based exercise analysis
-   🧍 Human pose detection using MediaPipe
-   🔢 Automatic repetition counting
-   📊 Set and workout progress tracking
-   🧠 Exercise-specific form analysis
-   🎤 AI voice coaching and feedback
-   🔊 Text-to-speech workout guidance
-   💾 Workout history using SQLite
-   🔐 Login/session-based workout tracking
-   🎨 Modern dark UI

## 🏋️ Supported Exercises

-   Squats
-   Push-ups
-   Biceps Curls (Dumbbell)
-   Shoulder Press
-   Lunges
-   Deadlift
-   Tricep Extension
-   Lateral Raises
-   Bench Press

## 🛠️ Tech Stack

**UI:** Streamlit, HTML, CSS

**Computer Vision:** MediaPipe, OpenCV, NumPy

**AI / LLM:** Groq API, `openai/gpt-oss-120b`

**Voice:** gTTS

**Data:** Python, SQLite, Pandas

## 🧠 How It Works

``` text
Camera
   ↓
MediaPipe Pose Detection
   ↓
Exercise Detector
   ↓
Joint Angles + Movement Analysis
   ↓
Rep / Set Tracking
   ↓
Form Issue Detection
   ↓
AI Coaching
   ↓
Text-to-Speech
   ↓
Real-Time Feedback
```

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone https://github.com/meetcodesX/FormSync-AI-Gym-Coach.git
cd FormSync-AI-Gym-Coach
```

### 2. Create a virtual environment

Windows:

``` powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

``` env
GROQ_API_KEY=your_groq_api_key
```

Never commit `.env` or API keys to GitHub.

## ▶️ Run the Application

``` bash
streamlit run main.py
```

If the Windows Streamlit launcher has a path issue:

``` powershell
.env\Scripts\python.exe -m streamlit run main.py
```

Open:

``` text
http://localhost:8501
```

## 🎤 AI Voice Coaching

FormSync generates coaching feedback for events such as:

-   Workout started
-   Set completed
-   Workout completed
-   No pose detected
-   Ongoing form checks

The generated feedback is converted into speech using text-to-speech.

## 📊 Workout History

FormSync stores completed workout data locally using SQLite, including:

-   Exercise
-   Repetitions
-   Sets
-   Workout time
-   Date

## 🔐 Security

Recommended `.gitignore` entries:

``` gitignore
venv/
.venv/
.env
.streamlit/secrets.toml
__pycache__/
*.pyc
data.db
```

## 🌐 Live Demo

**Try FormSync:**\
https://ai-realtime-gym-coach.streamlit.app/

## 👨‍💻 Author

**Meet Sahu**

-   LinkedIn: https://www.linkedin.com/in/meetsahu/
-   GitHub: https://github.com/meetcodesX

## 🚀 Future Improvements

-   More exercise detectors
-   Improved form classification
-   Personalized workout plans
-   Progress analytics
-   Better voice interaction
-   Cloud-based workout history
-   Mobile-friendly experience
-   More advanced AI coaching

## 📄 License

This project is currently available for educational and portfolio
purposes.
