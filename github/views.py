from django.shortcuts import render
# from rest_framework import generics
from .models import *
# from .serializers import GithuberSerializer

# def Home(request):
#     if request.POST == 'POST':
#         print("hi")
#         return render(request, "test.html", {})
#     else:
# 	    return render(request, "home.html", {})



# class ListGithuberView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Githuber.objects.all()
#     serializer_class = GithuberSerializer

# class DetailGithuberView(generics.GenericAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = Githuber.objects.all()
#     serializer_class = GithuberSerializer