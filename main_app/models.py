from django.db import models


class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    average_lifespan = models.PositiveIntegerField()
    native_region = models.CharField(max_length=100)

    # This is the string representation of the model
    # if someone did print(finch) it would return the name
    def __str__(self):
        return self.name
