from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('heroes/', views.heroes, name='heroes'),
    path('heroes/add', views.create_hero, name='add_hero'),
    path('heroes/<int:pk>', views.show_hero, name='show_hero')

]
