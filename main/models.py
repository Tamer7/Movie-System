from django.db import models
from django.contrib.auth.models import User


class MovieClass(models.Model):
    """
    Class for creating a Movie Fields
    """
    # fields for the movie table
    title = models.CharField(max_length=300, null=False)
    year = models.CharField(max_length=300, null=True)
    poster = models.URLField(default=None, null=True)
    rating = models.FloatField(default=0)
    director = models.CharField(max_length=300, null=True)
    cast = models.CharField(max_length=800, null=True)
    description = models.TextField(max_length=5000)
    movie_id = models.CharField(max_length=300, null=True)
    

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Review(models.Model):
    """
    Class for creating a Review Fields
    """
    movie = models.ForeignKey(MovieClass, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username






