from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("ihalist/", views.ihalist, name="ihalist"),
    path("create/", views.create, name="ihalist"),

]
