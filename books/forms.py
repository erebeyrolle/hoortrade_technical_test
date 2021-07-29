from django import forms
from django.forms import ModelForm
from .models import Author, Book

# Book creation form 
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
# Author creation form
class AuthorCreate(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'