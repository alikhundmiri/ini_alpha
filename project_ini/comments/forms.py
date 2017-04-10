from django import forms

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    # parent_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(widget=forms.Textarea, label="", help_text="Enter your Answer here!. Please Always cite your sources at the end of answer!")

