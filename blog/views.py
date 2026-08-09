from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404


def blog_list(request):

    return render(request, "blog/blog_list.html",)


def blog_detail(request, slug):

    return render(request, "blog/blog_detail.html",)