from django.urls import path
from django.conf.urls import url
from .views import (
    GithubDetailAPIView,
    GithubListAPIView,
    Home,
)


urlpatterns = [
    path('',GithubListAPIView.as_view()),
    url(r'^(?P<acc>\w+)/$',GithubDetailAPIView.as_view()),
    url(r'^scrapping/(?P<acc>\w+)/$',Home.as_view()),
    # path('githubers/', ListGithuberView.as_view(), name="githubers-all")
    # path('')
]