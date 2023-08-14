from django.shortcuts import render

# Filler Finch Data
finches = [
    {
        "name": "Zebra Finch",
        "description": "The zebra finch is a small bird...",
        "image_url": "https://via.placeholder.com/150",
        "id": 1,
        "scientific_name": "Taeniopygia guttata",
        "average_lifespan": "5-7 years",
        "native_region": "Australia, Indonesia, East Timor",
    },
    {
        "name": "Gouldian Finch",
        "description": "The gouldian finch is known for its vibrant colors...",
        "image_url": "https://via.placeholder.com/150",
        "id": 2,
        "scientific_name": "Erythrura gouldiae",
        "average_lifespan": "6-8 years",
        "native_region": "Northern Australia",
    },
]


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finch_index(request):
    context = {"finches": finches}
    return render(request, "finches/index.html", context)


def finch_detail(request, finch_id):
    finch = finches[finch_id - 1]
    context = {"finch": finch}
    return render(request, "finches/detail.html", context)
