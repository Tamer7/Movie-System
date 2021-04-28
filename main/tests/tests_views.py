from django.test import TestCase, Client
from django.urls import resolve, reverse
from ..models import MovieClass, Review
from ..views import home, details, add_movies,edit_movies,delete_movie,add_review,edit_review,delete_review
import json


class TestView(TestCase):
    """
    This class tests the view functionality of the application
    We test the detail, and CRUD functionality of the application
    """

    # This is the setup function, where variables are set to constants 
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('main:home')
        self.add_movie_url = reverse('main:add_movies')
        self.class1 = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )
        # self.class2 = Review.objects.create(
        #     movie = 'Superman',
        #     comment = 'Great Movie',
        #     rating = 9, 
        # )
        self.delete_movie = reverse('main:delete_movie', args=['001'])
        self.edit_movies = reverse('main:edit_movies', args=['001'])
        self.add_review = reverse('main:add_review', args=['1'])


    # This case tests the home page using the reverse function
    def test_project_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')


    # This case tests the post request of adding movies successfully
    def test_project_add_movie_POST_adding_movie(self):

        movieclass = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )


        response = self.client.post(self.add_movie_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(movieclass.title, 'batman')



    # This case tests the results if no data is passed through    
    def test_project_add_movie_POST_no_data(self):

        movieclass = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )

        response = self.client.post(self.add_movie_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(movieclass.title.count('title'), 0)


    # This test case tests the DELETE method in deleting the movie successfully
    def test_project_delete_movie_DELETE(self):
        movieclass = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )

        response = self.client.delete(self.delete_movie, json.dumps({
            'id' : 1
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(movieclass.title.count('title'), 0)


    # This case tests the DELETE method with no valid id
    def test_project_delete_movie_DELETE_no_id(self):
        movieclass = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )

        response = self.client.delete(self.delete_movie)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(movieclass.title.count('title'), 0)


    # This case tests the post request of editing movies successfully  
    def test_project_edit_movie_POST_adding_edit(self):
    
        movieclass = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )


        response = self.client.post(self.edit_movies)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(movieclass.title, 'batman')
        self.assertEquals(movieclass.year, 2007)
        self.assertEquals(movieclass.director, 'Reeves')


    # This case tests the post request of editing movies without a valid id
    def test_project_edit_movie_POST_adding_edit_no_id(self):
        
        movieclass = MovieClass.objects.create(
            title = 'batman',
            year = 2007,
            director = 'Reeves',
        )


        response = self.client.post(self.edit_movies)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(movieclass.title.count('title'), 0)



    # def test_project_add_review_POST_adding_review(self):
    
    #     movieclass = MovieClass.objects.create(
    #         title = 'Superman',
    #         year = 2007,
    #         director = 'Reeves',
    #     )
    
    #     reviewclass = Review.objects.create(
    #         movie = movieclass,
    #         comment = 'Great Movie',
    #         rating = 9,
    #     )


    #     response = self.client.post(self.add_review)

    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(reviewclass.movie.title, 'Superman')
    #     self.assertEquals(reviewclass.comment, 'Great Movie')
    #     self.assertEquals(reviewclass.rating, 9)


    





