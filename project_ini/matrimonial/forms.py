from django import forms
from .models import mat_info
from pagedown.widgets import PagedownWidget


class PostOffer(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    description = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = mat_info
        fields = [
            "title",
            "email_address",
            "phone_contact",
            "your_gender",
            "your_age",
            "your_qualification",
            "search_age",
            "search_qualification",
            "search_settled",
            "description",
            "image",
            "detail_privacy",
            "terms_and_conditions",
            "Draft",
            "publish",
        ]