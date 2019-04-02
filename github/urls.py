from django.urls import path
from .views import ListGithuberView, Home


urlpatterns = [
    path('',Home, name='home'),
    path('githubers/', ListGithuberView.as_view(), name="githubers-all")
]