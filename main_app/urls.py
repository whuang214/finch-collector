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
    # favorite foods routes
    path("favorite_foods/", views.FavoriteFoodList.as_view(), name="favorite_foods"),
    path(
        "favorite_foods/<int:pk>/",
        views.FavoriteFoodDetail.as_view(),
        name="favorite_foods_detail",
    ),
    path(
        "favorite_foods/create/",
        views.FavoriteFoodCreate.as_view(),
        name="favorite_foods_create",
    ),
    path(
        "favorite_foods/<int:pk>/update/",
        views.FavoriteFoodUpdate.as_view(),
        name="favorite_foods_update",
    ),
    path(
        "favorite_foods/<int:pk>/delete/",
        views.FavoriteFoodDelete.as_view(),
        name="favorite_foods_delete",
    ),
    # associate a favorite food with a finch (M:M)
    path(
        "finches/<int:finch_id>/assoc_favorite_food/<int:favorite_food_id>/",
        views.assoc_favorite_food,
        name="assoc_favorite_food",
    ),
    path(
        "finches/<int:finch_id>/unassoc_favorite_food/<int:favorite_food_id>/",
        views.unassoc_favorite_food,
        name="unassoc_favorite_food",
    ),
]
