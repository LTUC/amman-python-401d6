from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Person
from .forms import PersonCreationForm

class PersonAdmin(UserAdmin):
    add_form = PersonCreationForm
    model = Person
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = ((None,{'fields':('username', 'email', 'first_name', 'last_name', 'password')}),)

# Register your models here.
admin.site.register(Person, PersonAdmin)