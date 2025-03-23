Django Project with MySQL Database

This is a Django project configured to use a MySQL database.

🚀 Prerequisites

Python 3.x

Django

MySQL

pip (Python package manager)

MySQLclient or mysql-connector-python

🛠️ Project Setup

1. Clone the Repository

git clone <repository-url>
cd <project-directory>

2. Create and Activate a Virtual Environment

python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Database

Ensure MySQL is installed and running.

Create a database in MySQL:

CREATE DATABASE mydatabase;

Update the settings.py with your MySQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Run Migrations

python manage.py makemigrations
python manage.py migrate

6. Create Superuser

python manage.py createsuperuser

Follow the prompts to set a username, email, and password.

7. Start the Server

python manage.py runserver

Visit http://localhost:8000 in your browser.
