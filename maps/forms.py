from django import forms
#import floppyforms as forms

class AddressForm(forms.Form):
    address = forms.CharField()