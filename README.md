# 🚀 AI Invoice Tracker
> A simple web app that extracts invoice data from images using Gemini AI and stores results in Google Sheets.

![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

<!-- ## 🌐 Live Demo
* 🔗 **App Link:** *Add your deployed URL here*
* 📸 **Video Demo / GIF:** *Add a YouTube/Loom link or embed a GIF* -->

<!-- --- -->

## ✨ Key Features
* **Invoice Extraction:** Upload an invoice image; Gemini‑2.5‑flash‑lite extracts date, reference number, merchant name, and amount.
* **Google Sheet Integration:** Extracted data is automatically appended to a Google Sheet.
* **Invoice Image Storage:** Uploaded invoice images are securely stored using Supabase Storage integration.
* **Responsive UI:** Simple HTML/CSS/JS front‑end works on desktop and mobile.

---

## 🛠️ Tech Stack & Architecture
| Section     | Technology |
|:----------|:----------|
| **Frontend** | HTML, JavaScript (Fetch API), CSS |
| **Backend**  | FastAPI (Python), Uvicorn |
| **AI Service** | Gemini 2.5 Flash Lite (Google GenAI) |
| **Storage**   | Google Sheets API, Supabase Storage |
| **DevOps**    | virtualenv |

> **Why choose this stack?**
> FastAPI provides async support ideal for handling file uploads and external API calls. Gemini offers accurate OCR & data extraction without needing a custom model. Google Sheets gives a lightweight, instantly shareable datastore.

---

## 🚀 How to Run the Project (Local Setup)

### Prerequisites
* Python 3.11+ (virtualenv recommended)
* Node.js (optional, only for serving static files)
* Google Cloud credentials with `GEMINI_API_KEY` and Sheets API access
* Supabase Account & Project (with Bucket access for image storage)

### Installation Steps
1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/ai-invoice-tracker.git
   cd ai-invoice-tracker/AI-Invoice-Tracker
   ```
2. **Create and activate virtual environment**
   ```bash
   python -m venv invoice-track-env
   # Linux/macOS
   source invoice-track-env/bin/activate
   # Windows (PowerShell)
   .\invoice-track-env\Scripts\Activate.ps1
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   - Copy `config/credentials.json.example` to `config/credentials.json` and fill in your Google service‑account JSON.
   - Create a `.env` file in the project root and populate the following keys:
     ```bash
     GEMINI_API_KEY=your_gemini_api_key
     SUPABASE_URL=https://your-project-ref.supabase.co
     SUPABASE_KEY=your_supabase_anon_or_service_role_key
     SUPABASE_BUCKET_NAME=your_bucket_name
     ```
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
│  ├─ services/        # Integrations: Gemini AI, Google Sheets, & Supabase
│  └─ schemas/         # Pydantic models
├─ frontend/           # Simple HTML/JS UI
│  ├─ index.html
│  ├─ script.js        # Handles file upload & API call
│  └─ style.css
├─ config/             # Credentials & env files
└─ README.md           # Documentation (this file)
```
