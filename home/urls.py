from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("faqs/", views.faqs, name="faqs"),
    path("contact/", views.contact, name="contact"),
    path("appointment/", views.appointment, name="appointment"),
    path("doctor_profile/", views.doctor_profile, name="doctor_profile"),
    path("services/", views.services, name="services"),




]