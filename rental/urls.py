from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index, name='homePage'),
    path('home', views.index, name='homePage'),
    path('about', views.about, name='aboutPage'),
    path('catalog', views.catalog, name='catalogPage'),
    path('login', views.soon, name='loginPage'),
    path('order', views.soon, name='loginPage'),
    path('movie/<int:movie_id>', views.details, name="details"),
]