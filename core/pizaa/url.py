from django.urls import path , re_path
from .views import MainPage
urlpatterns = [
    re_path(r'^$',MainPage.as_view() ,name="index"),
]
