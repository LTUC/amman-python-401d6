from django.contrib.auth.forms import UserCreationForm
from .models import Person

class PersonCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')    
