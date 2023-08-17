from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
)


class Food(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food_detail", kwargs={"pk": self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    favorite_foods = models.ManyToManyField(Food)

    # This is the string representation of the model
    # if someone did print(finch) it would return the name
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # finch_detail is the "name" of the route
        return reverse("finch_detail", kwargs={"finch_id": self.id})
        # this returns a URL of the detail page (first argument) with the id of the finch (second argument)

    # this is a custom method that returns true if the finch has been fed today (all 3 meals)
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    class Meta:
        # change the plural name of the model to finches instead of finchs
        verbose_name_plural = "finches"


class Feeding(models.Model):
    date = models.DateField()
    # make a meal a choice of breakfast, lunch, or dinner (should be B, L, or D)
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # on delete means if the finch is deleted, delete the feeding with id of finch_id
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    # define dunder str to return a string representation of the model
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
        # get_meal_display works by taking the first letter of the meal and returning the second value in the tuple (how django processes tuple choices)

    # meta data for the model
    class Meta:
        # you can order by date in descending order
        ordering = ["-date"]
        # you can change the plural name of the model
        # verbose_name_plural = "feedings"
        # look up the docs for more meta options
