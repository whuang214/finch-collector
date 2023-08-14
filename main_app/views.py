from django.shortcuts import render
from .models import Finch


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finch_index(request):
    # get the data from the database
    fitches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": fitches})


def finch_detail(request, finch_id):
    fitch = Finch.objects.get(id=finch_id)
    return render(request, "finches/detail.html", {"finch": fitch})
