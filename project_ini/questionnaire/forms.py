from django import forms
from django.forms import Textarea
from .models import questions_info
from pagedown.widgets import PagedownWidget

class PostQuestion(forms.ModelForm):
    question = forms.TextInput()
    publish = forms.DateField(widget=forms.SelectDateWidget)
    detail = forms.CharField(widget=PagedownWidget, required=False)
    class Meta:
        model = questions_info
        fields = [
            "question",
            "detail",
            "draft",
            "publish",
        ]
