from django import forms
from models import GueatBookNew

class GuestBookForm(forms.ModelForm):

    class Meta:
        model = GueatBookNew
        fields = ('First_Name','Last_Name')
