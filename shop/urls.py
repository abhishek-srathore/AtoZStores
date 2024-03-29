from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="shopHome"),
    path("about/", views.about, name="aboutUs"),
    path("contact/", views.contact, name="contactUs"),
    path("search/", views.search, name="search"),
    path("prodView/<int:myid>", views.prodView, name="prodView"),
    path("checkout/", views.checkout, name="checkout"),
    path("tracker/", views.tracker, name="tracker"),
]
