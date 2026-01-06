# 🗳️ Public Opinion Portal

A Django-based web application that allows citizens to share and view public opinions for the **13th National Parliamentary Election (2026)** in Bangladesh. The project focuses on clean UI, constituency-wise opinions, and simple data management using SQLite.

<p>
  🎥 <strong>Project Overview Video</strong><br>
    <a href="https://jumpshare.com/share/xxQLnpp1p4b9YIyaIiJv" target="_blank">
    https://jumpshare.com/share/xxQLnpp1p4b9YIyaIiJv
    </a>
    <br>
    or
    <br>
     <a href="https://streamable.com/lne4dc" target="_blank">
    https://streamable.com/lne4dc
    </a>
</p>

<hr>

---

## 📌 Features

* Submit public opinions (name, election area, support party)
* View **Latest Opinions** (Latest add 3 items)
* View **All Opinions** with the same modern card layout
* Party-based color indication (BNP, Jamaat, Independent, No Comment)
* Responsive modern UI (desktop, tablet, mobile)
* SQLite database (default Django setup)
* Data can be managed via Django shell or DB Browser for SQLite

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML5, CSS3 (custom modern UI)
* **Database:** SQLite (`db.sqlite3`)
* **Tools:** Django Admin (optional), Django Shell, DB Browser for SQLite

---

## 📂 Project Structure

```text
opinion_project/
├── manage.py
├── db.sqlite3
├── opinion_project/
│   ├── settings.py
│   ├── urls.py
│   └── __pycache__/
├── opinions_app
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── templates/
│   └── migrations/
│   └─── static/
│       └── css/
└── templates/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/proalamin/pre-industry-program.git
cd pre-industry-program/Week\ 4/
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\\Scripts\\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 🧑‍💻 Admin Access (Optional)

Create a superuser:

```bash
python manage.py createsuperuser
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

> Note: Admin is optional. The project can be fully managed using Django shell or SQLite browser.

---

## 🗄️ Database Information

* **Database file:** `db.sqlite3`
* **Main table:** `opinions_opinion`
* Data persists unless explicitly deleted

### View Data Using Django Shell

```bash
python manage.py shell
```

```python
from opinions.models import Opinion
Opinion.objects.all()
```

### View Data Visually (Recommended)

* Install **DB Browser for SQLite**
* Open `db.sqlite3`
* Browse table: `opinions_opinion`

---

## 🧪 Dummy Data Management

### Delete All Opinion Data

```python
from opinions.models import Opinion
Opinion.objects.all().delete()
```

### Insert 10 Dummy Records

```python
from opinions.models import Opinion

data = [
    ("Rahim Uddin", "Dhaka-10", "BNP"),
    ("Karim Ahmed", "Dhaka-7", "Independent"),
    ("Hasan Ali", "Chattogram-5", "Jamaat"),
    ("Abdul Malek", "Sylhet-3", "BNP"),
    ("Nasir Hossain", "Rajshahi-4", "No Comment"),
    ("Imran Khan", "Bogura-6", "BNP"),
    ("Saiful Islam", "Pabna-3", "Jamaat"),
    ("Mahmudul Hasan", "Barishal-2", "Independent"),
    ("Anisur Rahman", "Rangpur-5", "BNP"),
    ("Arif Hossain", "Gazipur-2", "No Comment"),
]

for name, area, party in data:
    Opinion.objects.create(name=name, election_area=area, party=party)
```

---

## 🎨 UI & Design Notes

* Opinion cards displayed in grid layout
* Party colors:

  * **BNP:** Red
  * **Jamaat:** Green
  * **Independent:** Blue
  * **No Comment:** Gray
* Fully responsive design

---

## 🚀 Future Improvements

* Pagination for All Opinions
* Search & filter by constituency or party
* Charts & analytics
* Authentication for opinion submission
* REST API integration

---

## 👤 Author

**Md Al Amin**
Computer Science & Engineering Student

---

## 📜 License

This project is for **educational and learning purposes**.

---

✅ *End of Documentation*
