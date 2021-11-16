# Model

- in the terminal: 
    - mkdir snacks_project
    - cd snack_project
    - poetry init  -n 
    - poetry add django
    - poetry add --dev black flake8
    - poetry shell
    - django-admin startproject  snack_tracker_project
    - cd snack_tracker_project
    - python manage.py migrate
    - python manage.py startapp snacks
    - add `snacks` app to the `INSTALLED_APPS` in settings.py
    - open models.py inside `snacks`
    - create a class model `Snack` make this model inherit from : `models.Model`
    - name = models.CharField(max_length = 64)
    - from django.contrib.auth import get_user_model
    - purchaser = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    - description = models.TextField()
    - Admin:
      - from .models import Snack
      - admin.site.register(Snack)
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver


# View

- cd to to snacks app
- open views.py and there we can define our views
- create a list view for snacks `SnackListView`:
    - from django.views.generic import ListView, DetailView then extend the view from that
    - template_name = `"snack_list.html"`
    - from .models import Snack
    - model = Snack

- Create a detail view :
  - from 