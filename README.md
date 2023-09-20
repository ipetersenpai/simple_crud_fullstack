# simple_crud_fullstack implementation

This project is about Todo list application that let the user to create, read, update and delete.
The project use Django alone (both frontend and backend) and it use Mysql for the database.

### Project prototype link
https://www.figma.com/file/CRbRADDSsn7gEetNQ9jINl/todolist-robante?type=design&mode=design&t=vmDm2BYCL2uGpQ0F-0

## Installation guide
Make sure to have pipenv, python and django installed on your device.

## Important:
Do not change the port of the mysql and django always set it on the Port:3306(default mysql port) and Port: 8000 (default django port).
### Step: 1
Activate your environment in order to run the following command.

### Step: 2
I used django tailwind for the styling. install the following command below.
```
  python -m pip install django-tailwind
```
```
  python -m pip install "django-tailwind[reload]"
```
```
  python manage.py tailwind install
```
### Step: 3
Run the migrations command below to apply migrations and to create the detabase schema.
```
python manage.py migrate
```
### Step: 4
Run the code below to collect static files.
```
 python manage.py collectstatic
```
### Step: 5
Build the django tailwind in order to work the project.
```
 python manage.py tailwind start
```
### Step: 6
Finally, Open another terminal to run the django server. Do not close the current terminal that tailwind is running.
```
 python manage.py runserver
```

### Documentation
If you are encountering errors on the installation especially in django tailwind, please refer to the documentation link provided.
https://django-tailwind.readthedocs.io/en/latest/installation.html

