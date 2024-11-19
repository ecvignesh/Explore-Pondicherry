from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date']


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(widget=forms.HiddenInput())
