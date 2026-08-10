from django.shortcuts import render

from .models import (
    HeroSlider,Setting,About
)


def home(request):

    hero_sliders = HeroSlider.objects.filter(is_active=True).prefetch_related("buttons")

    settings_obj = Setting.objects.first()

    return render(
        request,
        "home/index.html",
        {
            "hero_sliders": hero_sliders,
            "settings_obj": settings_obj,
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
