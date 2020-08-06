from django import forms
from .models import Profile

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'location',
            'position',
            'image_url',
            'company',
        ]
      

      