from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget

class BlogForm(forms.ModelForm):
    detail = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "detail",
            "image",
            "draft",
            "publish",
        ]