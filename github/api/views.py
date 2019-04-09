from github.models import *

from django.views.generic import View
from django.http import HttpResponse

import json

from github.utils import AutoScrapping

from github.forms import GithuberForm

class Home(View):
    def get(self, request, acc, *args, **kwargs):
        qs = Githuber.objects.filter(useracc=str(acc)).first()
        if qs is None:
            cp = AutoScrapping(acc) # "nguyenkhacbaoanh"
            user = cp.infoPerso()
            form = GithuberForm(user)

            if form.is_valid():
                obj = form.save(commit=True)
                obj_json = obj.serialize()
                return HttpResponse(obj_json, content_type="application/json")
            if form.errors:
                error = json.dumps(form.errors)
                return HttpResponse(error, content_type="application/json")
        else:
            data_json = qs.serialize()
            return HttpResponse(data_json, content_type="application/json")

class GithubDetailAPIView(View):
    def get(self, request, acc, *args, **kwargs):
        # cp = AutoScrapping("https://github.com/nguyenkhacbaoanh")
        # user = cp.infoPerso()
        user = Githuber.objects.filter(useracc=str(acc)).first()
        if user is None:
            return HttpResponse(json.dumps({"message":"Not Found"}), content_type="application/json")
        user_json = user.serialize()
        return HttpResponse(user_json, content_type="application/json")

class GithubListAPIView(View):
    def get(self, request, *args, **kwargs):
        # cp = AutoScrapping("https://github.com/nguyenkhacbaoanh")
        # user = cp.infoPerso()
        user = Githuber.objects.all()#filter(useracc="nguyenkhacbaoanh")
        user_json = user.serialize()
        return HttpResponse(user_json, content_type="application/json")
