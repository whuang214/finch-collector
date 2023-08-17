from django.forms import ModelForm, DateInput
from django import forms
from .models import Feeding


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ["date", "meal"]
        widgets = {
            "date": DateInput(
                attrs={"class": "form-control datepicker", "id": "datepicker"}
            ),
            "meal": forms.Select(attrs={"class": "form-control"}),
        }
