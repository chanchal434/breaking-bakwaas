# 📰 Breaking Bakwaas – AI Satirical News Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-orange.svg)](https://ai.google.dev/gemini-api)

**Breaking Bakwaas** is a fun, AI‑powered web application that generates **satirical fake news** (“Bakwaas” = nonsense in Hindi). Built with Flask and Google Gemini, it lets you create hilarious news articles either by providing custom inputs or by using an auto‑generate mode. Each story comes with an AI‑generated image, downloadable PDF, and social sharing options.

> ⚠️ **Disclaimer** – This project is purely for **entertainment and satire**. All generated content is fictional and not meant to be taken as real news.

---

## ✨ Features

- **🎭 Two generation modes**  
  - *Custom mode*: Provide a topic, headline, or style – get a tailor‑made fake news story.  
  - *Auto mode*: Let the AI pick a random absurd topic and generate a complete news piece.

- **🖼️ AI‑generated images** – Each article gets a unique, matching image created by an AI model (Gemini or external image API).

- **📄 PDF export** – Download any news article as a beautifully formatted PDF for offline sharing or laughs.

- **📱 Social sharing** – One‑click share on Twitter, Facebook, or LinkedIn with a pre‑filled caption and link.

- **🗄️ Persistent storage** – Generated news items are stored in a local SQLite database (via `db_handler.py`) for later retrieval.

- **🎨 Modern UI** – Responsive, clean interface built with HTML, CSS, and JavaScript.

---

## 🛠️ Tech Stack

| Category       | Technologies                                                                 |
|----------------|-------------breaking-bakwaas/
├── app.py # Main Flask application entry point
├── ai_handler.py # Wrapper for Google Gemini API calls (text & images)
├── db_handler.py # SQLite database CRUD operations
├── requirements.txt # Python dependencies (create if missing)
├── .env # Environment variables (API keys) – not committed
├── LICENSE # MIT License
├── README.md # This file
├── static/ # Static assets (CSS, JS, images)
│ ├── style.css
│ └── script.js # all javascript which make it dynamic
├── templates/ # HTML templates
│ ├── index.html # Homepage (input form / auto mode)
│ ├── single_news.html # Individual article view with image & actions
│ └── (other .html files)
└── code_structure.txt # Legacy structure reference


-----------------------------------------------------------------|
| Backend        | Python 3.8+, Flask                                                           |
| AI & Generation| Google Gemini API (text generation), Image generation API (Gemini or custom) |
| Database       | SQLite (via `sqlite3` and custom `db_handler`)                              |
| Frontend       | HTML5, CSS3, JavaScript (Vanilla)                                           |
| PDF Generation | ReportLab / WeasyPrint (whichever implemented)                              |
| Deployment     | Local server / any WSGI server (Gunicorn, Waitress)                         |

---

## 📁 Project Structure

breaking-bakwaas/
├── app.py # Main Flask application entry point
├── ai_handler.py # Wrapper for Google Gemini API calls (text & images)
├── db_handler.py # SQLite database CRUD operations
├── requirements.txt # Python dependencies (create if missing)
├── .env # Environment variables (API keys) – not committed
├── LICENSE # MIT License
├── README.md # This file
├── static/ # Static assets (CSS, JS, images)
│ ├── style.css
│ └── script.js
├── templates/ # HTML templates
│ ├── index.html # Homepage (input form / auto mode)
│ ├── single_news.html # Individual article view with image & actions
│ └── (other .html files)
└── code_structure.txt # Legacy structure reference

## 🚀 Getting Started

- Python 3.8 or higher
- A [Google Gemini API key](https://ai.google.dev/gemini-api) (free tier available)
- (Optional) An image generation API key if not using Gemini for images – e.g., **Imagen**, **Stable Diffusion**, or **Pollinations.ai** (check `ai_handler.py` for details).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chanchal434/breaking-bakwaas.git
   cd breaking-bakwaas
