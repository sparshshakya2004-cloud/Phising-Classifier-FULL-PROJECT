# PhishLens Frontend Suite

This directory contains all user interface applications for the PhishLens Phishing Threat Scanner.

## 📁 Directory Structure
```
frontend/
├── app.py               # Flask Web Server (Serves soft-theme HTML/CSS/JS frontend)
├── streamlit_app.py     # Streamlit Interactive Security Dashboard
└── static/              # Web assets for Flask App
    ├── index.html       # Main HTML Interface & Maliciousness Rating Indicator
    ├── style.css        # Soft, eye-calming light-slate CSS theme
    └── app.js           # Dynamic scanner & rating meter logic
```

## 🚀 How to Run the Applications

### 1. Launch Flask Web Frontend
```bash
python frontend/app.py
```
Open your web browser at: **http://127.0.0.1:5000**

### 2. Launch Streamlit Dashboard
```bash
streamlit run frontend/streamlit_app.py
```
Open your web browser at: **http://localhost:8501**
