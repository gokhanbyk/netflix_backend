from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login_page"),
    path('register/', register_view, name='register_page'),
    path('profiles/', profile_page_view, name="profile_page"),
]
