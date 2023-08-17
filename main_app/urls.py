from django.urls import path  # import path function from django.urls
from . import views  # importing views.py from main_app

# all routes for this app
urlpatterns = [
    # home routes
    path("", views.home, name="home"),  # setting the route for the home page
    path("about/", views.about, name="about"),  # setting the route for the about page
    # finches routes
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
    # foods routes
    path("foods/", views.FoodList.as_view(), name="foods"),
    path(
        "foods/<int:pk>/",
        views.FoodDetail.as_view(),
        name="food_detail",
    ),
    path(
        "foods/create/",
        views.FoodCreate.as_view(),
        name="food_create",
    ),
    path(
        "foods/<int:pk>/update/",
        views.FoodUpdate.as_view(),
        name="food_update",
    ),
    path(
        "foods/<int:pk>/delete/",
        views.FoodDelete.as_view(),
        name="food_delete",
    ),
    # associate a favorite food with a finch (M:M)
    path(
        "finches/<int:finch_id>/assoc_foods/<int:food_id>/",
        views.assoc_food,
        name="assoc_food",
    ),
    path(
        "finches/<int:finch_id>/unassoc_foods/<int:food_id>/",
        views.unassoc_food,
        name="unassoc_food",
    ),
    path("accounts/signup/", views.signup, name="signup"),
]
