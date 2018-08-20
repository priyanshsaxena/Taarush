from django import forms

from .models import Blog, User

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body',)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_name', 'password',)