from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import GithuberSerializer
# Create your views here.

def Home(requests):
	return render(requests, "home.html", {})

class ListGithuberView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Githuber.objects.all()
    serializer_class = GithuberSerializer
