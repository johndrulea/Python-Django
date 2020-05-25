from django.contrib import admin
from .models import Movie, Genre


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name" )
    list_display_links = ("id", )

class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "genre")
    list_display_links = ("id", "title")
    #exclude = ("price",)
    fields = ("release_year", "title", "trailer", "image" ,"genre", "price", "in_stock")

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)

