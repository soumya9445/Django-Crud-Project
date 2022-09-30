from pyexpat import model
from django import forms
from myapp.models import UserModel
                                            

class UserForm(forms.ModelForm):
      no=forms.IntegerField()
      name=forms.CharField()
      class Meta:
            model=UserModel
            fields="__all__"            