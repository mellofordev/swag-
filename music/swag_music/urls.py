from django.urls import path

from . import views

urlpatterns = [
    path('song/', views.song, name='song'),

]