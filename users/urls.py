from django.urls import path
from .views import home, register, login, logout,profile,profile_edit,post_detail,create_post,edit_post,delete_post,my_blogs

urlpatterns = [
    path("", home, name="home"),  # Home Page
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", profile_edit, name="profile_edit"),  # New Edit Page
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', create_post, name='create_post'),
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
]
