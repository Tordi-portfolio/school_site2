from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Result, StudentUser, Post, Classroom
from datetime import datetime
from .forms import ProfileUpdateForm, BlogPostForm, StudentRegistrationForm, ResultUploadForm

# Create your views here.

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def upload_result_view(request):
    selected_class_id = request.GET.get('classroom') or request.POST.get('classroom')
    form = None

    if request.method == 'POST':
        form = ResultUploadForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.student = form.cleaned_data['student']
            result.save()
            messages.success(request, "Result uploaded successfully.")
            return redirect('upload_result')
    elif selected_class_id:
        form = ResultUploadForm(data={'classroom': selected_class_id})  # Pre-fill for filtering

    return render(request, 'upload_result.html', {
        'form': form,
        'classrooms': Classroom.objects.all(),
        'selected_class_id': selected_class_id
    })


# Profile picture view
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})
# End of profile picture view


@user_passes_test(lambda u: u.is_superuser)
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully.")
            return redirect('news')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', {'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html', {'year': datetime.now().year})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def dashboard(request):
    student = request.user
    results = Result.objects.filter(student=student).order_by('year', 'term')

    # Create a dict to hold: result => position
    positions = {}

    for result in results:
        same_term_results = Result.objects.filter(
            student__classroom=student.classroom,
            year=result.year,
            term=result.term
        )
        ranked = sorted(same_term_results, key=lambda r: r.total_score(), reverse=True)
        position = ranked.index(result) + 1 if result in ranked else None
        positions[result.id] = position

    return render(request, 'dashboard.html', {
        'student': student,
        'results': results,
        'positions': positions
    })


# @login_required
# def dashboard(request):
#     student = request.user
#     result = Result.objects.filter(student=student).first()
#     all_results = Result.objects.filter(student__classroom=student.classroom)
#     ranked = sorted(all_results, key=lambda r: r.total_score(), reverse=True)
#     position = ranked.index(result) + 1 if result in ranked else None
#     return render(request, 'dashboard.html', {'student': student, 'result': result, 'position': position})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user: login(request, user); return redirect('index')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')