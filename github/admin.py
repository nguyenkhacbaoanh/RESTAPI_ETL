from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Githuber)
admin.site.register(Repository)
admin.site.register(Star)
admin.site.register(Follower)
admin.site.register(Following)