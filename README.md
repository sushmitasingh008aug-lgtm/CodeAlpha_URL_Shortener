# CodeAlpha URL Shortener

A simple URL Shortener web application developed as part of the **CodeAlpha Backend Development Internship**.

This project converts long URLs into short, unique URLs and stores the URL mapping in a PostgreSQL database. When a user opens the generated short URL, the application redirects them to the original URL.

---

## Project Overview

The URL Shortener provides both a backend API and a simple web interface for creating shortened URLs.

The backend is developed using **Python Flask**, while **PostgreSQL** is used for storing URL mappings. Swagger is integrated for API documentation and testing.

---

## Objectives

- Create a backend server using Flask.
- Accept long URLs through an API.
- Generate unique short codes.
- Store URL mappings in PostgreSQL.
- Redirect users from short URLs to original URLs.
- Provide Swagger API documentation.
- Provide a simple frontend interface.

---

## Features

- Shorten long URLs.
- Generate unique 6-character short codes.
- Store URLs in PostgreSQL.
- Redirect short URLs to original URLs.
- Collision checking for generated short codes.
- REST API using Flask.
- Swagger API documentation.
- Simple frontend interface.
- JavaScript-based API requests.
- Basic error handling.

---

## Technologies Used

### Backend

- Python
- Flask
- Psycopg2
- PostgreSQL
- Python-dotenv
- Flasgger

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Visual Studio Code
- PostgreSQL
- pgAdmin
- Git
- GitHub
- Swagger UI

---

## Project Structure

```text
CodeAlpha_url_shortener/
│
├── app.py
├── database.py
├── routes.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

How the Application Works

The application follows this flow:

    User enters a long URL
        ↓
Frontend sends POST request
        ↓
Flask Backend
        ↓
Generate unique short code
        ↓
Store URL mapping in PostgreSQL
        ↓
Return short URL
        ↓
User opens short URL
        ↓
Flask searches PostgreSQL
        ↓
Redirects to original URL

Installation and Setup
1. Clone the Repository
git clone https://github.com/sushmitasingh008aug-lgtm/CodeAlpha_URL_Shortener.git

Move into the project directory:
cd CodeAlpha_URL_Shortener

2. Create a Virtual Environment
python -m venv venv

3. Activate the Virtual Environment
For Windows:
venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

PostgreSQL Configuration
Install and start PostgreSQL on your system.
Create a database named:
url_shortener

Then create the urls table using the SQL provided above.
Environment Variables
The application uses a .env file for PostgreSQL connection details.
Create a .env file in the root directory:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=url_shortener
DB_USER=postgres
DB_PASSWORD=your_postgresql_password

Replace your_postgresql_password with your own PostgreSQL password.
A .env.example file is included in the repository to show the required environment variable format.



