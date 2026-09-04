from django.urls import path
from . import views

app_name = "learning"

urlpatterns = [
    path("", views.subject_list, name="subject_list"),
    path(
        "subject/<slug:slug>/",
        views.material_list,
        name="material_list"
    ),
    path(
        "material/<slug:slug>/",
        views.material_detail,
        name="material_detail"
    ),
]