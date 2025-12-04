from django.contrib import admin
from django.urls import path, include
from users.views import RegisterView, ProfileView, LoginView


urlpatterns = (
    [
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='token_obtain_pair'),
        path("profile/", ProfileView.as_view()),
    ]
)
