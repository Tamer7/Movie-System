from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg
import requests


def home(request):
    """
    This function uses an api to get various movies depending on most popular movie selections
    Once the Search Bar is clicked it filters all the movies from the api and adds it to the 
    database automatically. 
    The "get_or_create()" function ensures identical movies are being added to the database. 

    """
    query = request.GET.get("title")
    all_movies = None
    if query:
        name = request.GET['title']
        # url = 'http://www.omdbapi.com/?apikey=7531b4db&s='+name+''
        url = 'https://api.themoviedb.org/3/search/movie?api_key=73b26cd6e71f57e195d7a253e3911b74&language=en-US&query=' + \
            name+'&page=1&include_adult=false'
        response = requests.get(url)
        data = response.json()
        movies = data['results']
        poster_link = 'https://image.tmdb.org/t/p/w500'

        for i in movies:
            movie_data = MovieClass.objects.get_or_create(
                title=i['original_title'],
                year=i['release_date'],
                rating=i['vote_average'],
                poster=poster_link + str(i['poster_path']),
                description=i['overview']
            )
            all_movies = MovieClass.objects.all().order_by('-id')
            all_movies = MovieClass.objects.filter(title__icontains=query)

    else:
        url_display = 'https://api.themoviedb.org/3/movie/popular?api_key=73b26cd6e71f57e195d7a253e3911b74&language=en-US&page=1&'
        response = requests.get(url_display)
        data = response.json()
        movies = data['results']
        poster_link = 'https://image.tmdb.org/t/p/w500'

        for i in movies:
            movie_data = MovieClass.objects.get_or_create(
                title=i['original_title'],
                year=i['release_date'],
                rating=i['vote_average'],
                poster=poster_link + str(i['poster_path']),
                description=i['overview']
            )
            all_movies = MovieClass.objects.all().order_by('-year')

    context = {
        "all_movies": all_movies,
    }

    return render(request, 'main/index.html', context)


# Displaying movie information
def details(request, id):
    """

    This view selects all the exisiting data from the database depending
    on the specific movie clicked, using the id parameter. Then displays 
    relevant information about the movie. 

    """
    movie = MovieClass.objects.get(id=id)  # select * from movie where id=id
    reviews = Review.objects.filter(movie=id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "movie": movie,
        "reviews": reviews,
        "average": average
    }

    return render(request, 'main/details.html', context)


# Adding movies to the database
def add_movies(request):
    """
    This function allows admin users to add specific movies 
    to the database. This functions checks weather the request
    is a POST and if it is, it validates the form values and adds
    it to the database. After adding a movie the admin is redirected
    to the Home page. 

    """

    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = MovieForm(request.POST or None)

                # check if the form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:home")
            else:
                form = MovieForm()
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add Movies"})

        # if they are not admin
        else:
            return redirect("main:home")

    # if they are not loggedin
    return redirect("accounts:login")


# Editing specific movies in the database
def edit_movies(request, id):
    """
    This function allows the admin to edit specific movies 
    The movie is retrieved based on the id and the exisiting
    information from the database is shown in the forms, which
    can be edited and saved.

    """

    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the movies linked with id
            movie = MovieClass.objects.get(id=id)

            # form check
            if request.method == "POST":
                form = MovieForm(request.POST or None, instance=movie)
                # check if form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = MovieForm(instance=movie)
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Edit Movies"})
        # if they are not admin
        else:
            return redirect("main:home")

    # if they are not loggedin
    return redirect("accounts:login")


# Deleting movies in the database
def delete_movie(request, id):
    """
    This function allows the admin to delete any
    specific movie based on the id and then redirected
    to the Home page.

    """

    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the moveis
            movie = MovieClass.objects.get(id=id)

            # delte the movie
            movie.delete()
            return redirect("main:home")
        # if they are not admin
        else:
            return redirect("main:home")

    # if they are not loggedin
    return redirect("accounts:login")


# Adding a review - ONLY AUTHENTICATED USERS
def add_review(request, id):
    """
    This function allows registered users to add
    a review on any specific movie. Users input
    the comment and rating of their choice.

    """

    if request.user.is_authenticated:
        movie = MovieClass.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form": form})
    else:
        return redirect("accounts:login")


# Editing the review
def edit_review(request, movie_id, review_id):
    """
    This allows users to edit their reviews based 
    on the specific movie_id and the review_id. 

    """

    if request.user.is_authenticated:
        movie = MovieClass.objects.get(id=movie_id)
        # review
        review = Review.objects.get(movie=movie, id=review_id)

        # check if the review was done by the logged in user
        if request.user == review.user:
            # grant permission
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Out or range. Please select rating from 0 to 10."
                        return render(request, 'main/editreview.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("main:detail", movie_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', {"form": form})
        else:
            return redirect("main:details", movie_id)
    else:
        return redirect("accounts:login")


# Deleting the review
def delete_review(request, movie_id, review_id):
    """
    This allows the users to delete an exisiting review
    they placed. Users can only delete a review they posted
    
    """

    if request.user.is_authenticated:
        movie = MovieClass.objects.get(id=movie_id)
        # review
        review = Review.objects.get(movie=movie, id=review_id)

        # check if the review was done by the logged in user
        if request.user == review.user:
            # grant permission to delete
            review.delete()

        return redirect("main:detail", movie_id)

    else:
        return redirect("accounts:login")
