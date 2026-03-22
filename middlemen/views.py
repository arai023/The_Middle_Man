from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def homeView(request):
    """
    This view will return the home page of the logged in user; if a user is not logged in it will redirect to the loginView view
    """
    pass

def loginUser(request):
    """
    This view will login a user based on the form submitted by loginView
    """
    pass

def loginView(request):
    """
    This view will render the login page if the user is not authenticated, it will return the user to the home page if the user is already logged in
    """
    pass

def signupView(request):
    """
    This view will render the signup page if the user is not authenticated, it will return the user to the home page if the user is already logged in
    """
    pass

def signupUser(request):
    """
    This view will sign up a user based upon the form submitted by the signup view
    """
    pass