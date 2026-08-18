from django.shortcuts import render

from .models import (
    HeroSlider,Setting,About,USP,why_choose,technologies
)


def home(request):

    hero_sliders = HeroSlider.objects.filter(is_active=True).prefetch_related("buttons")
    about_us = About.objects.first()
    settings_obj = Setting.objects.first()
    usp = USP.objects.all()[:6]
    why_choose_data = why_choose.objects.all()[:6]
    our_technologies = technologies.objects.all()[:6]


    return render(
        request,
        "home/index.html",
        {
            "hero_sliders": hero_sliders,
            "settings_obj": settings_obj,
            "about_us": about_us,
            "usp": usp,
            "why_choose": why_choose_data,
            "our_technologies": our_technologies,

        }
    )


def about(request):

    settings_obj = Setting.objects.first()
    about_us = About.objects.first()


    return render(
        request,
        "home/about.html",
        {
            "settings_obj": settings_obj,
            "about_us": about_us,

        }
    )


def gallery(request):

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/gallery.html",
        {
            "settings_obj": settings_obj,
        }
    )


def faqs(request):

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/faqs.html",
        {
            "settings_obj": settings_obj,
        }
    )


def contact(request):

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/contact.html",
        {
            "settings_obj": settings_obj,
        }
    )


def appointment(request):

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/appointment.html",
        {
            "settings_obj": settings_obj,
        }
    )


def doctor_profile(request):

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/doctor_profile.html",
        {
            "settings_obj": settings_obj,
        }
    )


def services(request):

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/services.html",
        {
            "settings_obj": settings_obj,
        }
    )
