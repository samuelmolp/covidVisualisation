from unicodedata import name
from django.urls import path

from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path("stats/", views.stats, name="stats"),
    path("images/", views.images, name="images"),
    path("videos/", views.videos, name="videos"),
    path("about/", views.aboutData, name="aboutData"),

    #API ROUTE
    path("getData/<str:start_date>/<str:end_date>/<str:type>/<str:region>/", views.get_data, name="getData")
]

