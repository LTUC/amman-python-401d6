# Create Django project with poetry

 Almost every django project is created following the same steps.
 Follow the same steps in this cheetsheet to start any Django new project.
 Note that it is not the only way of structring a Django project but this one is common in terms of simple-mid size projects. It is always good to refer to [Django docs](https://docs.djangoproject.com/en/3.2/) if you ever needed help since their documentation is easy and straight forward.

## Create a project

- First, create a new directory and initialize poetry inside it

```sh
$mkdir project_name
$cd project_name
$poetry init -n
```

- Next, install django framework, black and flake8 [read PEP8 style guide](https://www.python.org/dev/peps/pep-0008) and activate the venv.

```sh
$poetry add django
$poetry add black flake8
$poetry shell
```

- Create a new Django project using the following command

```sh
$django-admin startproject project_name

```

- cd into project_name and verify that everything is working well by running the server and going to the localhost : `http://127.0.0.1:8000`

```sh
$python manage.py runserver
```

- Run migrations

```sh
python manage.py migrate
```

- Create a new app inside a django project

```sh
$python manage.py startapp app_name
```

- Head to `settings.py` inside the project directory and add the name of the created app to the `INSTALLED_APPS` list

- Go to the `TEMPLATES` in settings.py and add the base directory to the `DIRS`: `[BASEDIR /'templates']`

- cd to the main project directory and create `templates` folder inside it. This is where your templates should live.

## Important steps to remember when you create an app

- Create app : `python manage.py startapp app_name`

- Add app to the projects in `settings.py` --> 'INSTALLED_APPS'

- Add views in the `views.py` inside your app

- Create a `urls.py` file in your app and include it in the project `urls.py` file
  
- Add urlpattern in the app `urls.py`

- Add a template for the view

- Add tests
