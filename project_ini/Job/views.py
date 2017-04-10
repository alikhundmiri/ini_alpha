from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import job_database
from .forms import JobForm


def job_create(request):
    if not request.user.is_authenticated:  # or not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = JobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "New Job offer Created!!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
        "tab_text": "New Job",
        "top_text": "Creating New Job Offers",
        "form_text": "Please fill this form to add new Job Posting",
    }
    return render(request, 'general_form.html', context)


def job_detail(request, slug=None):
    today = timezone.now().date()
    this_job = get_object_or_404(job_database, slug=slug)
    if this_job.draft or this_job.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "title": "Job Description",
        'this_job': this_job,
        "today": today,
    }
    return render(request, 'job/job_detail.html', context)


def job_list(request):
    today = timezone.now().date()
    all_jobs_list = job_database.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        all_jobs_list = job_database.objects.all()

    query = request.GET.get("q")
    if query:
        all_jobs_list = all_jobs_list.filter(
            Q(title__icontains=query) |
            Q(detail__icontains=query)
        ).distinct()

    paginator = Paginator(all_jobs_list, 10)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_jobs = paginator.page(paginator.num_pages)

    context = {
        'all_jobs': all_jobs,
        'title': 'Jobs',
        'page_request_var': page_request_var,
        'today': today,
    }
    return render(request, 'job/job_index.html', context)


def job_update(request, slug=None):
    instance = get_object_or_404(job_database, slug=slug)
    if instance.user != request.user:
        raise Http404
    form = JobForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "New Job offer Created!!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
        "tab_text": "Edit Job Post",
        "top_text": "Edit Job Post",
        "form_text": "Make changes to the form here:",
        'this_job': instance,
    }
    return render(request, 'general_form.html', context)


def job_delete(request, slug=None):
    instance = get_object_or_404(job_database, slug=slug)
    if instance.user != request.user:
        raise Http404
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("jobs:list")
