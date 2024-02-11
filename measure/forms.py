from django import forms
from .models import UserMeasurement


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = UserMeasurement
        fields = ['height', 'chest_size', 'waist_size']
        # Add other measurement fields as needed
