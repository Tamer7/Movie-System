from django.test import SimpleTestCase
from ..forms import MovieForm,ReviewForm


class TestForms(SimpleTestCase):
    """
    Testing Class for the Adding movie forms
    and adding review forms
    """

    # This function tests that the data inputed in the form is valid - MOVIE FORM
    def test_movie_form_valid_data(self):
        form = MovieForm(data={
            "title" : "Batman",
            "year" : 2010,
            "poster" : "google.com",
            "rating" : 9,
            "director" : "Nolan",
            "cast" : "Chris",
            "description" : "Amazing",
        })

        self.assertTrue(form.is_valid())


    # This function tests that an error shows if there is no data passed to the form - MOVIE FORM
    def test_movie_form_no_data(self):
        form = MovieForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)


    # This function tests that the data inputed in the form is valid - REVIEW FORM
    def test_review_form_valid_data(self):
        form = ReviewForm(data={

            "comment" : "amazing",
            "rating" : 9,
        })

        self.assertTrue(form.is_valid())


    # This function tests that an error shows if there is no data passed to the form - REVIEW FORM
    def test_review_form_no_data(self):
        form = ReviewForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
