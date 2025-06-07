from django.urls import path
from . import views
from .views import upload_result_view

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-result/', upload_result_view, name='upload_result'),

    path('news', views.news, name='news'),
    path('post/<str:pk>', views.post, name='post')
]