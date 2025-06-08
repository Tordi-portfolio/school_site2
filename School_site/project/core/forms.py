from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StudentUser, Classroom
from .models import Profile
from .models import Result, StudentUser, Post

class StudentRegistrationForm(UserCreationForm):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), required=True)
    class Meta:
        model = StudentUser
        fields = ['first_name', 'last_name', 'username', 'email', 'classroom', 'password1', 'password2']

class ResultUploadForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=StudentUser.objects.all(), required=True)
    class Meta:
        model = Result
        exclude = []

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


# Profile Picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']