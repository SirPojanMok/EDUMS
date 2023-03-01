from django import forms
from .models import Item


class BuyItemForm(forms.Form):

    quantity = forms.IntegerField(min_value=1)


    
