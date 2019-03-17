from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'user_id', 
            'ministry_name',
            'ministry_location',
            'county',
            'email',
            'address',
            'phone_number',
            'ministry_location',
            'description',
            'booking_date',
            'return_date',
            )