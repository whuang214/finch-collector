from django.urls import path  # import path function from django.urls
from . import views  # importing views.py from main_app

# all routes for this app
urlpatterns = [
    path("", views.home, name="home"),  # setting the route for the home page
    path("about/", views.about, name="about"),  # setting the route for the about page
    path(
        "finches/", views.finch_index, name="finches"
    ),  # setting the route for the all finches page
    path("finches/<int:finch_id>/", views.finch_detail, name="finch_detail"),
    path("finches/create/", views.FinchCreate.as_view(), name="finches_create"),
    path(
        "finches/<int:pk>/update/", views.FinchUpdate.as_view(), name="finches_update"
    ),
    path(
        "finches/<int:pk>/delete/", views.FinchDelete.as_view(), name="finches_delete"
    ),
    path("finches/<int:finch_id>/add_feeding/", views.add_feeding, name="add_feeding"),
]
