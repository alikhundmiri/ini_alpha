from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import mat_info
from .forms import PostOffer

def mat_create(request):
    if not request.user.is_authenticated:# or not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostOffer(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "tab_text": "New Matrimonial",
        "top_text": "Create New Matrimonial Offer",
        "form_text": "Please fill in all the blanks. These data will be made available for public viewing",
    }
    return render(request, 'general_form.html', context)

def mat_detail(request, slug=None):
    today = timezone.now().date()
    instance = get_object_or_404(mat_info, slug = slug)
    if instance.Draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "title" : "Details of Proposals",
        "instance" : instance,
        "today" : today,
    }
    return render(request, 'matrimonial/mat_detail.html', context)


def mat_list(request):
    today = timezone.now().date()
    all_list = mat_info.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        all_list = mat_info.objects.all()

    query = request.GET.get("q")
    if query:
        all_list = all_list.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)|
            Q(email_address__icontains=query)|
            Q(phone_contact__icontains=query)|
            Q(your_gender__icontains=query)|
            Q(search_settled__icontains=query)|
            Q(your_age__icontains=query)|
            Q(your_qualification__icontains=query)
        ).distinct()

    paginator = Paginator(all_list, 10) # Show 25 contacts per page
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

    context = {
        'title': 'Matrimonials',
        'all_list': queryset,
        'page_request_var': page_request_var,
        'today' : today,
    }
    return render(request,'matrimonial/mat_index.html', context)

def mat_update(request, slug=None):
    instance = get_object_or_404(mat_info, slug=slug)
    if instance.user != request.user:
        raise Http404
    form = PostOffer(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "tab_text": "Edit Matrimonial Post",
        "top_text": "Edit your Matrimonial Offer",
        "form_text": "Please make change to the details in the fields provided below.",
        "all_list": instance
    }
    return render(request, 'general_form.html', context)

def mat_delete(request, slug=None):
    instance = get_object_or_404(mat_info, slug=slug)
    if instance.user != request.user:
        raise Http404
    instance.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect("matrimonial:list")