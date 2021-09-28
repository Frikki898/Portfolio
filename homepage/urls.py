from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name="homepage_index"), #localhost:3000/
]
