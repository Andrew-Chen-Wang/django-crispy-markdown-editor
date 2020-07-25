from django.urls import path
from . import views
urlpatterns = [
    path("", views.blah, name="blah")
]