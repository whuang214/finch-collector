from django.urls import path  # import path function from django.urls
from . import views  # importing views.py from main_app

# all routes for this app
urlpatterns = [
    path("", views.home, name="home"),  # setting the route for the home page
    path("about/", views.about, name="about"),  # setting the route for the about page
    path(
        "finches/", views.finches_index, name="finches"
    ),  # setting the route for the all finches page
]
