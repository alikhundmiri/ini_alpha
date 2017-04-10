from django.shortcuts import render
from matrimonial.models import mat_info
from Job.models import job_database
from questionnaire.models import questions_info
from posts.models import Post
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    return render(request, 'mainpage/lander.html')

def photos(request):
    return render(request, 'mainpage/photo_s.html')

def profile(request):
    today = timezone.now().date()

    mat_list = mat_info.objects.filter(mat_info.user == User)
    job_list = job_database.objects.active()
    qna_list = questions_info.objects.active()
    blg_list = Post.objects.active()
    # if request.user.is_staff or request.user.is_superuser:
    #     job_list = job_database.objects.all()
    #     qna_list = questions_info.objects.all()
    #     blg_list = Post.objects.all()
    #
    context = {
        "mat": mat_list,
        "job": job_list,
        "qna": qna_list,
        "blg": blg_list,
    }
    return render(request, 'mainpage/user_profile.html', context)