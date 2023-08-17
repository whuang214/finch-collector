from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic import ListView, DetailView
from .models import Finch, Food
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
    finch = Finch.objects.get(id=finch_id)
    # make a feeding form
    feeding_form = FeedingForm()

    # get all foods from the database that are not in the finch's favorite foods
    # pass them in to the template
    foods_finch_doesnt_have_in_favorites = Food.objects.exclude(
        id__in=finch.favorite_foods.all().values_list("id")
    )

    return render(
        request,
        "finches/detail.html",
        {
            "finch": finch,
            "feeding_form": feeding_form,
            "foods": foods_finch_doesnt_have_in_favorites,
        },
    )


# GET request to display the create form
# Should return a html page <appname>/<model_name>_form.html by default
# while passing in a form object into the template
class FinchCreate(CreateView):
    model = Finch
    fields = "__all__"
    success_url = "/finches/"

    # override the get_form method to add bootstrap classes to the form fields
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs["class"] = "form-control"
        form.fields["description"].widget.attrs["class"] = "form-control"
        form.fields["image_url"].widget.attrs["class"] = "form-control"
        return form


# GET request to display the update form
# Passes in the finch object into the template
# the finch object has all the fields we need to display in the form
# POST request to process the update form
class FinchUpdate(UpdateView):
    model = Finch
    fields = [
        "description",
        "image_url",
    ]

    # override the get_form method to add bootstrap classes to the form fields
    def get_form(self, form_class=None):
        # get the form from the parent class
        form = super().get_form(form_class)
        # add bootstrap classes to the form fields
        form.fields["description"].widget.attrs["class"] = "form-control"
        form.fields["image_url"].widget.attrs["class"] = "form-control"
        # normally will just return the form but we want to add a custom label
        return form


# GET request to display the confirmation page
# POST request to delete the finch
class FinchDelete(DeleteView):  # inherits from DeleteView
    model = Finch
    success_url = reverse_lazy("finches")


# POST request to add a feeding to a finch
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


# automatically handle get and post requests
# GET will display the form
# POST will process the form
class FoodList(ListView):
    model = Food
    template_name = "foods/index.html"


# get will display the form
class FoodDetail(DetailView):
    model = Food
    template_name = "foods/detail.html"


# get will display the form
# post will process the form
class FoodCreate(CreateView):
    model = Food
    fields = "__all__"
    success_url = reverse_lazy("foods")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, field in form.fields.items():
            field.widget.attrs["class"] = "form-control"
        return form


class FoodUpdate(UpdateView):
    model = Food
    fields = ["name"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, field in form.fields.items():
            field.widget.attrs["class"] = "form-control"
        return form


class FoodDelete(DeleteView):
    model = Food
    success_url = reverse_lazy("foods")


def assoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).favorite_foods.add(food_id)
    return redirect("finch_detail", finch_id=finch_id)


def unassoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).favorite_foods.remove(food_id)
    return redirect("finch_detail", finch_id=finch_id)
