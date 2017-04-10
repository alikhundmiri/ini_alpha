from django import forms
from .models import job_database
from pagedown.widgets import PagedownWidget


class JobForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    detail = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = job_database
        fields = [
            "title",
            "detail",
            "image",
            "contact_email",
            "contact_number",
            "draft",
            "publish",

        ]