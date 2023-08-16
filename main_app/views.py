from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finch_index(request):
    # get the data from the database
    fitches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": fitches})


def finch_detail(request, finch_id):
    # get the data from the database
    fitch = Finch.objects.get(id=finch_id)
    # make a feeding form
    feeding_form = FeedingForm()

    return render(
        request, "finches/detail.html", {"finch": fitch, "feeding_form": feeding_form}
    )


# GET request to display the create form
# Should return a html page <appname>/<model_name>_form.html by default
# while passing in a form object into the template


# POST request to process the create form
class FinchCreate(CreateView):  # inherits from CreateView
    model = Finch  # model is the model we are using
    fields = "__all__"  # all fields in the model
    success_url = "/finches/"  # where to go after creating a new finch


# GET request to display the update form
# Passes in the finch object into the template
# the finch object has all the fields we need to display in the form


# POST request to process the update form
class FinchUpdate(UpdateView):  # inherits from UpdateView
    model = Finch
    fields = [
        "description",
        "image_url",
    ]


# GET request to display the confirmation page
# POST request to delete the finch
class FinchDelete(DeleteView):  # inherits from DeleteView
    model = Finch
    success_url = "/finches"


def add_feeding(request, finch_id):
    # add a feeding to the database
    form = FeedingForm(request.POST)
    if form.is_valid():
        # don't save the form to the db until it has the finch_id assigned
        # b/c right now it is just a form with a date and mealtime no finch_id
        new_feeding = form.save(commit=False)
        # assign the finch to the feeding
        new_feeding.finch_id = finch_id
        new_feeding.save()

    return redirect("finch_detail", finch_id=finch_id)
