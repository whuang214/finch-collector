from django.urls import path # import path function from django.urls
from . import views # importing views.py from main_app

# all routes for this app
urlpatterns = [
    path('', views.home, name='home'), # setting the route for the home page
]

