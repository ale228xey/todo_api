from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, UserLoginView, UserRegistrationView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),
    path('update-task/<int:pk>', TaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<int:pk>', TaskDeleteView.as_view(), name='delete-task'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),


]
