from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login_page"),
    path('register/', register_view, name='register_page'),
    path('profiles/', profile_page_view, name="profile_page"),
    path('profile-add/', profile_add_view, name="profile_add_page"),
    path('profile-edit/<slug:profile_slug>/', profile_edit_view, name="profile_edit_page"),
    path('profile-delete/<slug:profile_slug>/', profile_delete_view, name="profile_delete_page"),
]
