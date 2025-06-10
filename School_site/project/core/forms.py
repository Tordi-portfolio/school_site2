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
    classroom = forms.ModelChoiceField(
        queryset=Classroom.objects.all(),
        required=True,
        label="Class"
    )
    student = forms.ModelChoiceField(
        queryset=StudentUser.objects.none(),
        required=True,
        label="Student"
    )

    class Meta:
        model = Result
        exclude = []

    def __init__(self, *args, **kwargs):
        super(ResultUploadForm, self).__init__(*args, **kwargs)

        # Support GET and POST data
        data = self.data or self.initial
        class_id = data.get('classroom')

        if class_id:
            try:
                class_id = int(class_id)
                self.fields['student'].queryset = StudentUser.objects.filter(classroom_id=class_id)
                self.fields['classroom'].initial = class_id
            except (ValueError, TypeError):
                self.fields['student'].queryset = StudentUser.objects.none()
        else:
            self.fields['student'].queryset = StudentUser.objects.none()


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body','picture', 'video']


# Profile Picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']