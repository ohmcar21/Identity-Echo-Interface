# 📡 Identity Echo Interface

A beginner-friendly **Streamlit** application that collects a user's name and message,
validates the inputs, and echoes the transmission back — complete with a token-count estimate.

---

## 📁 Project Structure

```
Mirai Assignment/
├── app.py            ← Main Streamlit application
├── requirements.txt  ← Python dependencies
└── README.md         ← This file
```

---

## 🚀 How to Run

### 1 — Prerequisites

Make sure you have **Python 3.8 or higher** installed.  
Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

Verify your installation:
```bash
python --version
```

---

### 2 — (Optional but Recommended) Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS / Linux)
source venv/bin/activate
```

---

### 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs `streamlit` and its dependencies.

---

### 4 — Run the App

```bash
streamlit run app.py
```

Streamlit will start a local development server and automatically open the app in your
default browser at **http://localhost:8501**.

---

## 🎮 How to Use the App

| Step | Action |
|------|--------|
| 1 | Enter your **Name** in the first input field |
| 2 | Type your **Message** in the second input field |
| 3 | Click **🚀 Transmit** |
| ✅ | If both fields are filled, you'll see a success confirmation and token estimate |
| ⚠️ | If the message is empty, a warning is shown |
| ❌ | If the name is empty, an error is shown |

---

## 🧠 How Token Estimation Works

The app uses a simple approximation:

```
token_count = len(message) / 4
```

This is based on the industry rule-of-thumb that **1 token ≈ 4 characters** of English text
(as used by OpenAI and similar LLM providers).

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Python](https://python.org) | Core language |
| [Streamlit](https://streamlit.io) | Web UI framework |

---

## 📝 Notes

- No external API keys or database required — fully local.
- The app reruns from top to bottom every time you interact with it (this is normal Streamlit behaviour).
- To stop the server, press `Ctrl + C` in your terminal.
