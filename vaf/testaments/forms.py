from django import forms

from .models import Testament

class TestamentForm(forms.ModelForm):
    class Meta:
        model = Testament
        fields = (
            'partner',    
            'ministry_name' ,
            'message',
            )
    
    