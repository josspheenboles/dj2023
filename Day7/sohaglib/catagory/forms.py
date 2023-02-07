from django import forms
from .models import Catagory
class CatagoryForm(forms.Form):
    name=forms.CharField(label='Catagory_name',initial='plapsls')


'''
class CatagoryForm2(forms.ModelForm):
    class Meta:
        model=Catagory
        fileds='__all__'
'''

