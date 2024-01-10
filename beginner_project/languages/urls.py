from django.urls import path
from . import views

urlpatterns = [
    path("", views.home.as_view(), name="home"),
    path("about/", views.about.as_view(), name="about"),
    path("python/", views.python.as_view(), name="python"),
    path("fsharp/", views.fsharp.as_view(), name="fsharp"),
    path("racket/", views.racket.as_view(), name="racket"),
]
