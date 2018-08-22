from django import forms

from .models import Blog, User

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body', 'category')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_name', 'password',)
        widgets = {
	        'password': forms.PasswordInput(),
	    }

class LoginForm(forms.Form):

	user_name = forms.CharField(label='User name', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
