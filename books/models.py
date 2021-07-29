from django.conf import settings
from django.db import models

# Library classes & methods creation #
#------------------------------------#

# Authors class creation
class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
# Method to Convert Author object in string for console admin & pyshell visualization #
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

# Books class creation
class Book(models.Model):
    cover = models.ImageField(upload_to="", verbose_name='Couverture')
    title = models.CharField(max_length=255, verbose_name='Titre')
    summary = models.TextField('Résumé du livre')
    publication = models.DateField('Date de parution')
    pages = models.IntegerField('Nbre de pages')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Auteur')
# Method to Convert Book object in string for pyshell visualization #
    # def __str__(self):
    #     return "%s %s %s %s %s %s " % (self.cover, self.title, self.summary, self.publication, self.pages, self.author)