# 💸 Expense Tracker (Django)

A modern, dark-themed **Expense Tracker web application** built using **Django**.  
The project allows users to securely manage their daily expenses with authentication, a clean dashboard, and a futuristic UI.

---

## 🚀 Features

- 🔐 User Authentication (Sign Up / Login / Logout)
- 👤 User-specific expenses (each user sees only their own data)
- ➕ Add new expenses
- 🗑️ Delete expenses
- 📊 Dashboard showing total spending
- 🌙 Dark futuristic UI
- 🧩 Template inheritance using `base.html`
- 🎨 Clean, GitHub-ready CSS structure

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Dark UI)
- **Database:** SQLite (default Django DB)
- **Authentication:** Django built-in User model
- **Styling:** Custom CSS (no external frameworks)

---

## 📂 Project Structure
```text
expense_tracker/
│
├── tracker/
│   ├── migrations/
│   ├── static/
│   │   └── tracker/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── expense_list.html
│   │   └── add_expense.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## ⚙️ Installation & Setup

1️⃣ Clone the repository
```
git clone https://github.com/your-username/expense-tracker-django.git
cd expense-tracker-django
```
2️⃣ Create a virtual environment
```
python -m venv env
env\Scripts\activate
```

3️⃣ Install dependencies
```
pip install django
```
4️⃣ Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
5️⃣ Start the server
```
python manage.py runserver
```
6️⃣ Open in browser
```
http://127.0.0.1:8000/
```
## 📈 Future Enhancements

- ✏️ Edit existing expenses
- 📅 Monthly and category-wise filters
- 📊 Charts and analytics dashboard
- 🌐 Deployment on cloud (Render / Railway / Heroku)
- 📱 Improved mobile responsiveness

## 👨‍💻 Author

**Aaditya Siddharth Bansod**  
B.Tech Computer Science Engineering  
Django & Flask Certification Project  

This project was built as part of a Django certification course to understand
backend development, authentication, and clean UI design.
