from django.db import models
from django.contrib.auth.models import AbstractUser

from PIL import Image
from django.conf import settings


# Create your models here.

# Profile picture
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
# End Of Profile Picture



class Classroom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.name



class StudentUser(AbstractUser):
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)



class Result(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)

    TERM_CHOICES = [
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    ]

    term = models.CharField(max_length=20, choices=TERM_CHOICES)
    year = models.IntegerField()
    position = models.IntegerField(max_length=3)


    # Example: Maths
    maths_test1 = models.IntegerField(default=0)
    maths_test2 = models.IntegerField(default=0)
    maths_exam = models.IntegerField(default=0)
    @property
    def maths_total(self):
        return self.maths_test1 + self.maths_test2 + self.maths_exam

    english_test1 = models.IntegerField(default=0)
    english_test2 = models.IntegerField(default=0)
    english_exam = models.IntegerField(default=0)
    @property
    def english_total(self):
        return self.english_test1 + self.english_test2 + self.english_exam

    civic_test1 = models.IntegerField(default=0)
    civic_test2 = models.IntegerField(default=0)
    civic_exam = models.IntegerField(default=0)
    @property
    def civic_total(self):
        return self.civic_test1 + self.civic_test2 + self.civic_exam

    agric_test1 = models.IntegerField(default=0)
    agric_test2 = models.IntegerField(default=0)
    agric_exam = models.IntegerField(default=0)
    @property
    def agric_total(self):
        return self.agric_test1 + self.agric_test2 + self.agric_exam

    computer_test1 = models.IntegerField(default=0)
    computer_test2 = models.IntegerField(default=0)
    computer_exam = models.IntegerField(default=0)
    @property
    def computer_total(self):
        return self.computer_test1 + self.computer_test2 + self.computer_exam

    verbal_reasoning_test1 = models.IntegerField(default=0)
    verbal_reasoning_test2 = models.IntegerField(default=0)
    verbal_reasoning_exam = models.IntegerField(default=0)
    @property
    def verbal_reasoning_total(self):
        return self.verbal_reasoning_test1 + self.verbal_reasoning_test2 + self.verbal_reasoning_exam

    quantitative_test1 = models.IntegerField(default=0)
    quantitative_test2 = models.IntegerField(default=0)
    quantitative_exam = models.IntegerField(default=0)
    @property
    def quantitative_total(self):
        return self.quantitative_test1 + self.quantitative_test2 + self.quantitative_exam

    crs_test1 = models.IntegerField(default=0)
    crs_test2 = models.IntegerField(default=0)
    crs_exam = models.IntegerField(default=0)
    @property
    def crs_total(self):
        return self.crs_test1 + self.crs_test2 + self.crs_exam

    social_studies_test1 = models.IntegerField(default=0)
    social_studies_test2 = models.IntegerField(default=0)
    social_studies_exam = models.IntegerField(default=0)
    @property
    def social_studies_total(self):
        return self.social_studies_test1 + self.social_studies_test2 + self.social_studies_exam

    government_test1 = models.IntegerField(default=0)
    government_test2 = models.IntegerField(default=0)
    government_exam = models.IntegerField(default=0)
    @property
    def government_total(self):
        return self.government_test1 + self.government_test2 + self.government_exam

    def total_score(self):
        return (
            self.maths_total +
            self.english_total +
            self.civic_total +
            self.agric_total +
            self.computer_total +
            self.verbal_reasoning_total +
            self.quantitative_total +
            self.crs_total +
            self.social_studies_total +
            self.government_total
        )
    


from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.CharField(max_length=100, default=datetime.now, blank=True)