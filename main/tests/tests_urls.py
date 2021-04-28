
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from ..views import home, details, add_movies,edit_movies,delete_movie,add_review,edit_review,delete_review


class TestUrls(SimpleTestCase):

    """
    This Test case uses the reverse function to 
    check weather the correct url was used. 

    """
    
    # Unit testing for the home url 
    def test_home_url_is_resolved(self):
        url = reverse('main:home')
        self.assertEquals(resolve(url).func, home)

    # Unit testing for the detail url 
    def test_details_url_is_resolved(self):
        url = reverse('main:detail', args=['005'])
        self.assertEquals(resolve(url).func, details)

    # Unit testing for the add_movie url 
    def test_add_movie_url_is_resolved(self):
        url = reverse('main:add_movies')
        self.assertEquals(resolve(url).func, add_movies)

    # Unit testing for the edit_movie url 
    def test_edit_movie_url_is_resolved(self):
        url = reverse('main:edit_movies', args=['005'])
        self.assertEquals(resolve(url).func, edit_movies)

    # Unit testing for the delete_movie url 
    def test_delete_movie_url_is_resolved(self):
        url = reverse('main:delete_movie', args=['123'])
        self.assertEquals(resolve(url).func, delete_movie)

    # Unit testing for the add_review url 
    # def test_add_review_url_is_resolved(self):
    #     url = reverse('main:add_review', args=['123'])
    #     self.assertEquals(resolve(url).func, add_review)

    #  # Unit testing for the edit_review url 
    # def test_edit_review_url_is_resolved(self):
    #     url = reverse('main:edit_review', args=['005', '006'])
    #     self.assertEquals(resolve(url).func, edit_review)

    #  # Unit testing for the delete_review url 
    # def test_delete_review_url_is_resolved(self):
    #     url = reverse('main:delete_review', args=['123', '123'])
    #     self.assertEquals(resolve(url).func, delete_review)
