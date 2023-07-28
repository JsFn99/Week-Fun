from datetime import date
from django import forms
from .models import Event
from accounts.models import Customer


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "Name",
            "Slug",
            "Adresse",
            "Country",
            "Date",
            "Lowest_Price",
            "Highest_Price",
            "Availibility",
            "Description",
            "Image",
            "Category",
            "Trending",
            "Type",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["Slug"].initial = "personal"
        self.fields["Image"].required = False  
        self.fields["Image"].widget.attrs["accept"] = "image/*"  
        self.fields["Trending"].initial = False
        self.fields["Trending"].widget = forms.HiddenInput()
        self.fields["Type"].initial = "Private"
        self.fields["Type"].widget = forms.HiddenInput()
        self.fields["Date"].initial = date.today()

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'address2', 'country', 'state', 'zip_code']