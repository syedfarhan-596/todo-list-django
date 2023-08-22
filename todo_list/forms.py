from django import forms
from .models import TodoListModel
class ItemsForms(forms.ModelForm):
    class Meta:
        model= TodoListModel
        fields = ['item']