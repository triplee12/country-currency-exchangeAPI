# Application Setup Guide

## Overview

This document provides step-by-step instructions on how to run the application locally. The project uses **Python**, **FastAPI**, **SQLAlchemy**, and **MySQL**.

## Prerequisites

Before starting, ensure you have the following installed on your machine:

* **Python 3.10+**
* **MySQL Server** (running and accessible)
* **pip** (Python package manager)
* **virtualenv** (optional but recommended)

## Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/triplee12/country-currency-exchangeAPI.git
cd country-currency-exchangeAPI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your environment variables:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/your_db_name
HOST = "0.0.0.0"
PORT = 8000
RESTCOUNTRIES_URL = 'https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies'
EXCHANGE_URL = 'https://open.er-api.com/v6/latest/USD'
CACHE_DIR = 'cache'
```

## Database Setup

### 1. Create the Database

Login to MySQL and create a database:

```sql
CREATE DATABASE your_db_name;
```

## Running the Application

### 1. Start the Server

Run the FastAPI app using **uvicorn**:

```bash
uvicorn main:app --reload

# Or

python -m main
```

### 2. Access the Application

Open your browser and visit:

```bash
http://127.0.0.1:8000
```

### 3. API Documentation

FastAPI provides built-in interactive documentation:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Common Issues

* **MySQL fails to start** → Check MySQL logs with:

  ```bash
  sudo journalctl -u mysql.service -xe
  ```

* **Database connection error** → Verify credentials in `.env` and ensure the database is running.
* **ModuleNotFoundError** → Make sure your virtual environment is activated.

## Tech Stack

* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Migrations:** Alembic

## Author

Developed by **Chukwuebuka Emmanuel Ejie**. Contributions and feedback are welcome!
