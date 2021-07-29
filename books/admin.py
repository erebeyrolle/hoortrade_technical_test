""" 
    Models importation and registration in the admin console
    in order to populate the DB and control running
"""
from django.contrib import admin

# Author model importation
from .models import Author
admin.site.register(Author)

# Book model importation
from .models import Book
admin.site.register(Book)
