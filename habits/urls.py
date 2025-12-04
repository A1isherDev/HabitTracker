# from django.contrib import admin
from django.urls import path
from habits.views import HabitViewSet


urlpatterns = (
    [
        path('create/', HabitViewSet.as_view({'post': 'list'}), name='habit_create'),
    ]
)
