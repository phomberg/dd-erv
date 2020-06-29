from django.urls import path
from erv import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", views.login, name="login"),
    path("cust_index/", views.cust_index, name="cust_index"),
    path("cust_view/<id>", views.cust_view, name="cust_view"),
    path("requ_index/", views.requ_index, name="requ_index"),
    path("art_class/", views.art_class, name="art_class"),
]