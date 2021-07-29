from django.urls import path
from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static

from . import views

# app_name = 'books'
urlpatterns = [
    # Home page URL
    path('', views.home, name='home'),
    path('details/<int:book_id>', views.details, name='details'),
    path('create/', views.create_book, name = 'create_book'),
    path('details/update/<int:book_id>', views.update_book, name='update'),
    path('details/delete/<int:book_id>', views.delete_book, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url(r'', views.books_home, name='home'),
# ]