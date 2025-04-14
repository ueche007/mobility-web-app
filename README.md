# Mobility Web App – Flask Backend API

This is the backend Flask API for the DOM Mobility project developed by Ulysses Echeverria. It enables users to query and visualize data stored in a PostgreSQL database (`domdb`). The application provides a search interface to filter mobility-related chemical compound records and allows viewing corresponding fragment data via hyperlinks.

---

## 🚀 Features

- Filter mobility data by:
  - `mz_exp` (experimental m/z value)
  - `mz_calc` (calculated m/z value)
  - `mz_error_ppm` (parts-per-million error)
  - `chem_formula`
  - `origin`
- Clickable `mz_exp` values that link to matching fragment records
- Clean tabular HTML display for both mobility and fragment data
- Structured Python code with inline documentation
- Flask-based web server running locally

---

## 🧐 Author Notes

This code is written with clarity and future collaboration in mind. Each component of the code is documented to ensure maintainability. The application is designed to be easily integrated with a frontend component or extended for research workflows.

---

## 🛠️ Setup Instructions

### 🔧 Step 1: Clone the Repository

Open a terminal and clone the GitHub repository:

```bash
git clone https://github.com/pcdslab/mobility-web-app.git
cd mobility-web-app
```

### 🐍 Step 2: Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

If you're using Windows:
```bash
venv\Scripts\activate
```

### 📦 Step 3: Install Python Dependencies

Install the required libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, you can create it manually:

```bash
pip install Flask psycopg2
pip freeze > requirements.txt
```

---

## 🗄️ PostgreSQL Configuration

Ensure your PostgreSQL database is accessible with the following settings:

- **Host:** `localhost`
- **Port:** `5433`
- **Database:** `domdb`
- **User:** `domuser`
- **Password:** `Password`

These values are defined in `app.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'dbname': 'domdb',
    'user': 'domuser',
    'password': 'Password'
}
```

Ensure PostgreSQL is running and listening on port `5433`, and the `mobility_data` and `fragments_data` tables are properly loaded.

---

## ▶️ Running the Flask App

From the root of the repository:

```bash
python app.py
```

You should see an output like:

```
Running on http://127.0.0.1:8000
```

Now open your browser to:

```
http://127.0.0.1:8000/filter
```

---

## 🔗 Example Usage

1. Access `/filter` endpoint.
2. Provide values for `mz_exp`, `chem_formula`, and/or other filters.
3. Submit the form to see matching mobility records.
4. Click on a `mz_exp` value to view corresponding fragment records.

---

## 🤝 Contributing

This backend is part of a collaborative project. The frontend integration is managed by other team members. If you're extending the backend, feel free to open an issue or pull request.

To contribute:

```bash
git checkout -b feature-name
# Make your changes
# Commit and push
```

---

## 📚 License

MIT License or other license to be defined by the repository maintainer.

---
