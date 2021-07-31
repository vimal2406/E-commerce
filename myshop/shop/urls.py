from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="shopHome"),
    path("about",views.about, name="AboutUS"),
    path("contact",views.contact, name="ContactUS"),
    path("tracker",views.tracker, name="Tracker"),
    path("productview",views.productview, name="ProductView"),
    path("checkout",views.checkout, name="Checkout"),
    path("search",views.search, name="Search"),
]
