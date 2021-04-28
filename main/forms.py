from django import forms
from .models import *

# Movie add form
class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieClass
        fields = ('title', 'year', 'poster', 'rating', 'director', 'cast', 'description')

# Review add form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")