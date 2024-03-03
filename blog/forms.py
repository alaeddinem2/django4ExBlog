from django import forms
from .models import Comment



class EmailPostform(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=40)
    to = forms.EmailField(max_length=40)
    coments = forms.CharField(required=False,widget=forms.Textarea())


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']