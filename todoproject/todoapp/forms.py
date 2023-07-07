from . models import todo
from django import forms

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=todo
        fields=['name','priority','date']