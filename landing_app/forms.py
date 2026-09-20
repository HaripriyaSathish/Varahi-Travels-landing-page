import re
from datetime import date

from django import forms

from .models import Enquiry

LETTERS_ONLY = re.compile(r"^[A-Za-z\s]+$")


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            "pickup_location",
            "destination",
            "travel_date",
            "passengers",
            "vehicle_type",
            "phone_number",
            "name",
            "email",
            "message",
            "source",
        ]
        widgets = {
            "source": forms.HiddenInput(),
        }

    def clean_name(self):
        value = self.cleaned_data.get("name", "").strip()
        if value and not LETTERS_ONLY.match(value):
            raise forms.ValidationError("Letters only — no numbers or symbols.")
        return value

    def clean_pickup_location(self):
        value = self.cleaned_data.get("pickup_location", "").strip()
        if value and not LETTERS_ONLY.match(value):
            raise forms.ValidationError("Letters only — no numbers or symbols.")
        return value

    def clean_destination(self):
        value = self.cleaned_data.get("destination", "").strip()
        if value and not LETTERS_ONLY.match(value):
            raise forms.ValidationError("Letters only — no numbers or symbols.")
        return value

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"].strip()
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone

    def clean_travel_date(self):
        travel_date = self.cleaned_data.get("travel_date")
        if travel_date and travel_date < date.today():
            raise forms.ValidationError("Travel date cannot be in the past.")
        return travel_date

    def clean_passengers(self):
        passengers = self.cleaned_data.get("passengers")
        if passengers is not None and passengers < 1:
            raise forms.ValidationError("Passengers must be at least 1.")
        return passengers

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get("source")

        # Hero quick-enquiry requires the trip fields; the contact form
        # (source="contact") relies on name/email/message instead.
        if source == "hero":
            for field in ["pickup_location", "destination", "travel_date",
                          "passengers", "vehicle_type"]:
                if not cleaned_data.get(field):
                    self.add_error(field, "This field is required.")
        elif source == "contact":
            for field in ["name", "email", "pickup_location", "destination",
                          "travel_date", "passengers", "vehicle_type"]:
                if not cleaned_data.get(field):
                    self.add_error(field, "This field is required.")
        return cleaned_data