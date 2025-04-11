from django import forms
from .models import MeetingRequest

class MeetingRequestForm(forms.ModelForm):
    class Meta:
        model = MeetingRequest
        fields = ['teacher', 'preferred_date', 'message']
