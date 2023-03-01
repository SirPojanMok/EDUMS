from django import forms
from .models import Seller
from markets.models import Item

class CreateStoreForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ['account',]

class DeleteStoreForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'image', 'description', 'quantity', 'price']
