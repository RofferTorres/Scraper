# 🕸️ Basic Scraper Application

[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML](https://img.shields.io/badge/Frontend-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A simple **web scraping** application built with **Python** and **Django**.  
It allows you to extract and visualize data from web pages based on user-defined criteria.

---

## 🚀 Features

- 🧩 **Modular Design** — Easily extendable for new scraping rules or data models.  
- ⚙️ **Customizable** — Specify target URLs and custom extraction patterns.  
- 🧠 **Simple UI** — HTML-based interface to input URLs and view extracted data.  
- 💾 **Temporary Data Storage** — Extracted results are saved locally and displayed in a table.

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RofferTorres/Scraper.git
   ```

2. **Navigate into the project directory**

   ```bash
   cd Scraper
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. Define your scraping logic inside:  
   `mysite/myapp/views.py`

2. Run the Django application:

   ```bash
   cd ./mysite
   python manage.py runserver
   ```

3. Open your browser at:  
   👉 [http://localhost:8000/](http://localhost:8000/)

4. Enter your **target URL** in the web form.

5. The scraped data will be **temporarily saved** in the local database and **displayed in a table**.

---

## 🧾 License

This project is licensed under the **MIT License** — see the [LICENSE](https://github.com/RofferTorres/Scraper/blob/main/LICENSE) file for details.

---

## 📂 Project Structure

```
Scraper/
├── mysite/
│   ├── myapp/
│   │   ├── templates/
│   │   ├── views.py        # Scraping logic here
│   │   ├── models.py
│   │   └── ...
│   ├── manage.py
│   └── settings.py
├── requirements.txt
└── README.md
```

---

💡 **Tip:**  
You can extend this scraper by integrating libraries like `BeautifulSoup`, `Requests`, or `Scrapy` for more advanced extraction logic.
