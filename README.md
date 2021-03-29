# medical-report-system
A Django Rest Framework based system used for management and viewing of medical report of patients uploaded by doctors.

Installation
MRS requires DJANGO v3.1.7 or greater version to run.
Create project directory,
\medical-report-system> mkdir mrs
\medical-report-system> cd mrs
Before installing Django, it’s recommended to install Virtualenv that creates new isolated environments to isolates your Python files on a per-project basis. This will ensure that any changes made to your website won’t affect other websites you’re developing. The interesting part is that you can create virtual environments with different python versions, with each environment having its own set of packages.
\medical-report-system\mrs> python -m venv <env-name>
Start Virtual Environment,
Linux/Mac:
$ /mrs» source <env-name>/bin/activate
Windows:
\medical-report-system\mrs> .\<env-name>\Scripts\activate
Before starting the project, make sure your are on following versions,
(env) \medical-report-system\mrs> pip -V
pip 20.1.1 from d:\work\projects\django projects\medical-report-system\env\lib\site-packages\pip (python 3.8)
Now install the packages we require from requirement.txt with the command,
(env) \medical-report-system\mrs> pip install -r /path/to/requirements.txt


A project refers to the entire application and all its parts.
An app refers to a submodule of the project.
to start project named mis,
To make sure the installation is done properly, you will need to do the migrations first and then run the project.
(env) \medical-report-system\mrs> python manage.py makemigrations
No changes detected

Now we will run the migrate commands which will synchronize and create/modify the tables in database as per requirement.
(env) \medical-report-system\mrs> python manage.py migrate
To run migrations without affecting the database schema, you will need to do a fake migration.
(env) \medical-report-system\mrs> python manage.py migrate --fake

Finally, run the project.
(env) \medical-report-system\mrs> python manage.py runserver
this will start the dev server on 127.0.0.1:8000, where you will see the django-introduction page.

Database connections
For now SQLite3 database is used but this can be modified in settings.py file.

Migrations
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

It will go to settings.py and get INSTALLED_APPS
within these installed apps directory it will go to models and create schema for whatever class you have specified.

Project Developed by Pratik Patil.
