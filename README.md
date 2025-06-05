
# 🧭 Job Application Tracker App

A simple Flask-based web application to help users track their job applications. Users can register, log in, and manage job entries with details such as company name, position, status, notes, and deadlines.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Register and log in securely with hashed passwords
  - Session management using Flask

- 📋 **Job Management**
  - Add, edit, view, and delete job applications
  - Fields include company, position, status, notes, and deadline

- 👤 **User-Specific Dashboard**
  - Each user sees only their own job entries

---

## 🛠 Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Database:** PostgreSQL (or SQLite for development)
- **Frontend:** HTML5, Bootstrap, Jinja2 templates
- **Other:** Werkzeug for password hashing, Flask Blueprints for route separation


---

## 📂 Project Structure

```

JobTracker/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │    ├──__init__.py
│   │    ├──auth.py
|   |    └── jobs.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── jobs.html
|   ├── static/
│       └── style.css
├── config.py
├── run.py
├── requirements.txt
└── README.md

````

---

## 🧪 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/job-tracker.git
cd job-tracker
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (optional)

Create a `.env` file and add:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=your_postgresql_url
```

### 5. Initialize the Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the App

```bash
flask run
```

---

## 📦 Example Job Entry

* **Company:** Google
* **Position:** Software Engineer Intern
* **Status:** Applied / Interview / Offer / Rejected
* **Deadline:** 2025-06-20
* **Notes:** Hackathon project helped in shortlisting

---

## ✨ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Kashish Rajput**
[LinkedIn](https://www.linkedin.com/in/kashish-rajput-b5a344275) | [GitHub](https://github.com/kashishrajputt)

---



