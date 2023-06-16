from django.urls import path
from . import views

# url config
urlpatterns = [path("test1/", views.say_hello)]
