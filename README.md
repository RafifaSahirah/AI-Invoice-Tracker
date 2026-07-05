# 🚀 AI Invoice Tracker
> A simple web app that extracts invoice data from images using Gemini AI and stores results in Google Sheets.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

---

<!-- ## 🌐 Live Demo
* 🔗 **App Link:** *Add your deployed URL here*
* 📸 **Video Demo / GIF:** *Add a YouTube/Loom link or embed a GIF* -->

<!-- --- -->

## ✨ Key Features
* **Invoice Extraction:** Upload an invoice image; Gemini‑2.5‑flash‑lite extracts date, reference number, merchant name, and amount.
* **Google Sheet Integration:** Extracted data is automatically appended to a Google Sheet.
* **Responsive UI:** Simple HTML/CSS/JS front‑end works on desktop and mobile.

---

## 🛠️ Tech Stack & Architecture
| Section     | Technology |
|:----------|:----------|
| **Frontend** | HTML, JavaScript (Fetch API), CSS |
| **Backend**  | FastAPI (Python), Uvicorn |
| **AI Service** | Gemini 2.5 Flash Lite (Google GenAI) |
| **Storage**   | Google Sheets API |
| **DevOps**    | virtualenv |

> **Why choose this stack?**
> FastAPI provides async support ideal for handling file uploads and external API calls. Gemini offers accurate OCR & data extraction without needing a custom model. Google Sheets gives a lightweight, instantly shareable datastore.

---

## 🚀 How to Run the Project (Local Setup)

### Prerequisites
* Python 3.11+ (virtualenv recommended)
* Node.js (optional, only for serving static files)
* Google Cloud credentials with `GEMINI_API_KEY` and Sheets API access

### Installation Steps
1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/ai-invoice-tracker.git
   cd ai-invoice-tracker/AI-Invoice-Tracker
   ```
2. **Create and activate virtual environment**
   ```bash
   python -m venv invoice-track-env
   source invoice-track-env/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   - Copy `config/credentials.json.example` to `config/credentials.json` and fill in your Google service‑account JSON.
   - Set `GEMINI_API_KEY` in your shell or a `.env` file.
5. **Run the API**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will be available at `http://127.0.0.1:8000`.
6. **Open the frontend**
   Open `frontend/index.html` in a browser (or serve it with a simple static server).

---

## 📂 Project Structure
```
AI-Invoice-Tracker/
├─ app/                # FastAPI backend
│  ├─ main.py          # Entry point, defines /invoice/process
│  ├─ services/        # Gemini AI and Google Sheet integrations
│  └─ schemas/         # Pydantic models
├─ frontend/           # Simple HTML/JS UI
│  ├─ index.html
│  ├─ script.js        # Handles file upload & API call
│  └─ style.css
├─ config/             # Credentials & env files
└─ README.md           # Documentation (this file)
```
