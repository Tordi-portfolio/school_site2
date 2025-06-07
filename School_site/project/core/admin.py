from django.contrib import admin
from .models import StudentUser, Classroom, Result, Profile, Post

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Classroom)
admin.site.register(Result)
admin.site.register(Profile)
admin.site.register(Post)