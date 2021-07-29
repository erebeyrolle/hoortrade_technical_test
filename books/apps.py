""" 
    hoortrade project apps instantiation
    and declaration of their own namespace
"""

from django.apps import AppConfig

""" 
    app Books instantiation, 
    namespace declaration
"""

class BooksConfig(AppConfig):
    name = 'books'
