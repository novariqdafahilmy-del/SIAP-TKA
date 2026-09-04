from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "guru-dashboard/",
        views.guru_dashboard,
        name="guru_dashboard"
    ),

    path(
        "siswa-dashboard/",
        views.siswa_dashboard,
        name="siswa_dashboard"
    ),
]