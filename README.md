# 🔗 CodeAlpha URL Shortener

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-API%20Docs-85EA2D?logo=swagger&logoColor=black)

A URL shortener web application built with **Flask** and **PostgreSQL** as part of the **CodeAlpha Backend Development Internship**.

It converts long URLs into short, unique links, stores the mappings in a database, and redirects visitors from the short link to the original URL. It includes a REST API, interactive Swagger documentation, and a simple web interface.

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Database Schema](#-database-schema)
- [Troubleshooting](#-troubleshooting)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## ✨ Features

- Shorten long URLs through a REST API or web interface
- Unique 6-character short codes with collision checking
- Persistent storage in PostgreSQL (with a `UNIQUE` constraint on short codes)
- Fast redirection from short URL to original URL
- Interactive Swagger API documentation (Flasgger)
- Lightweight HTML/CSS/JavaScript frontend
- Basic error handling

---

## 🛠 Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python, Flask, Psycopg2, Python-dotenv, Flasgger |
| **Database** | PostgreSQL (managed with pgAdmin) |
| **Frontend** | HTML, CSS, JavaScript |
| **Tools** | VS Code, Git, GitHub, Swagger UI |

---

## 📁 Project Structure

```text
CodeAlpha_URL_Shortener/
│
├── app.py              # Application entry point
├── database.py         # PostgreSQL connection and queries
├── routes.py           # API and redirect routes
├── utils.py            # Helper functions (short code generation)
├── requirements.txt    # Python dependencies
├── .env.example        # Sample environment variables
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html      # Web interface
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ How It Works

```text
User enters a long URL
        ↓
Frontend sends POST /shorten request
        ↓
Flask backend generates a unique short code
        ↓
URL mapping is stored in PostgreSQL
        ↓
Short URL is returned to the user
        ↓
User opens the short URL (GET /<short_code>)
        ↓
Flask looks up the code in PostgreSQL
        ↓
User is redirected to the original URL
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL installed and running
- Git

### 1. Clone the repository

```bash
git clone https://github.com/sushmitasingh008aug-lgtm/CodeAlpha_URL_Shortener.git
cd CodeAlpha_URL_Shortener
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Create a PostgreSQL database named `url_shortener`:

```sql
CREATE DATABASE url_shortener;
```

Then connect to it and create the `urls` table:

```sql
CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5. Configure environment variables

Copy the example file and edit it:

```bash
cp .env.example .env        # macOS / Linux
copy .env.example .env      # Windows
```

Update `.env` with your PostgreSQL details:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=url_shortener
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

### 6. Run the application

```bash
python app.py
```

The app will be available at **http://127.0.0.1:5000**

---

## 💻 Usage

### Web interface

1. Open http://127.0.0.1:5000
2. Enter a long URL
3. Click **Shorten URL**
4. Copy or click the generated short URL to be redirected to the original page

### Swagger documentation

Interactive API docs are available at:

**http://127.0.0.1:5000/apidocs/**

You can test every endpoint directly from the browser.

---

## 📡 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/shorten` | Creates a short URL |
| `GET` | `/<short_code>` | Redirects to the original URL |

### `POST /shorten`

**Request body**

```json
{
    "url": "https://www.google.com"
}
```

**Response**

```json
{
    "original_url": "https://www.google.com",
    "short_code": "aB72xK",
    "short_url": "http://127.0.0.1:5000/aB72xK"
}
```

**Example with cURL**

```bash
curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'
```

### `GET /<short_code>`

Looks up the short code and redirects the browser to the original URL. If the code does not exist, an error response is returned.

---

## 🗄 Database Schema

**Database:** `url_shortener` | **Table:** `urls`

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `SERIAL` | Primary key | Auto-incrementing ID |
| `original_url` | `TEXT` | `NOT NULL` | The full original URL |
| `short_code` | `VARCHAR(20)` | `UNIQUE`, `NOT NULL` | Generated short code |
| `created_at` | `TIMESTAMP` | Default: `CURRENT_TIMESTAMP` | Creation time |

The `UNIQUE` constraint on `short_code` guarantees that no two URLs share the same code.

---

## 👩‍💻 Author

**Sushmita Singh** — [GitHub](https://github.com/sushmitasingh008aug-lgtm)

Developed as part of the **CodeAlpha Backend Development Internship**.

---

⭐ If you found this project useful, consider giving it a star!
