from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from .models import questions_info
from .forms import PostQuestion

from comments.models import Comment
from comments.forms import CommentForm

Current_User = get_user_model()
# Create your views here.
def qna_create(request):
    if not request.user.is_authenticated:# or not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostQuestion(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Question Asked succesfully, please visit us back to check if answer is ready!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "tab_text": "New Question",
        "top_text": "Ask us a new question!",
        "form_text": "You have the option to briefly description your question!",
    }
    return render(request, 'general_form.html', context)


def qna_detail(request, slug=None):
    today = timezone.now().date()
    can_comment = False
    if request.user.is_staff or request.user.is_superuser:
        can_comment = True
    instance = get_object_or_404(questions_info, slug=slug)
    if instance.draft or instance.publish > today:
        if not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    initial_data = {
        "content_type":instance.get_content_type,
        "object_id":instance.id,
    }
    # For new Comments
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data
        )
    comments = instance.comments
    context = {
        "title": "Question",
        "instance": instance,
        "today": today,
        "comments": comments,
        "comment_form": form,
        "can_comment":can_comment,
    }
    return render(request, 'questionnaire/qna_detail.html', context)


def qna_list(request):
    today = timezone.now().date()
    all_question = questions_info.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        all_question = questions_info.objects.all()
    query = request.GET.get("q")
    if query:
        all_question = all_question.filter(
            Q(question__icontains=query) |
            Q(detail__icontains=query)
        ).distinct()
    paginator = Paginator(all_question, 10)  # show 10 questions at a time on a single page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    comments = Comment.objects.all()
    context = {
        'title': "Questions and Answers",
        'all_question': queryset,
        'page_request_var': page_request_var,
        'today': today,
        "comments": comments,
    }
    return render(request, 'questionnaire/qna_index.html', context)


def qna_update(request, slug=None):
    instance = get_object_or_404(questions_info, slug=slug)
    if instance.user != request.user:
        raise Http404
    form = PostQuestion(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Question Edited!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "tab_text": "Edit Your Question",
        "top_text": "Editing Tools",
        "form_text": "Please make change to the question in the field provided below.",
        "all_question": instance
    }
    return render(request, 'general_form.html', context)


def qna_delete(request, slug=None):
    instance = get_object_or_404(questions_info, slug=slug)
    if instance.user != request.user:
        raise Http404
    instance.delete()
    messages.success(request, "Question Deleted Successfully!!!")
    return redirect("qna:list")
