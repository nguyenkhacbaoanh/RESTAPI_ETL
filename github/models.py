from django.db import models
from django.core.serializers import serialize

import json

# Create your models here.
class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        list_qs = list(self.values("useracc", "username", "bio", "location"))
        return json.dumps(list_qs)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

class Githuber(models.Model):
    useracc = models.CharField(max_length=255, null=False, unique=True)
    username = models.CharField(max_length=255, null=False)
    bio = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)

    objects = UpdateManager()

    def __str__(self):
        return '%s: %s' % (str(self.useracc), str(self.username))
    
    def serialize(self):
        json_data = serialize("json", [self], fields=["useracc", "username", "bio", "location"])
        stuct = json.loads(json_data)
        data = json.dumps(stuct[0]["fields"])
        return data

class Repository(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_repo', on_delete=models.CASCADE)
    repo = models.CharField(max_length=255, null=False)
    used_lang = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '%s: %s' % (str(self.repo), str(self.used_lang))


class Star(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_star', on_delete=models.CASCADE)
    repo_starred = models.CharField(max_length=255, null=False)
    used_lang_starred = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '%s: %s' % (str(self.repo_starred), str(self.used_lang_starred))

class Follower(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_follow', on_delete=models.CASCADE)
    followers_acc = models.CharField(max_length=255, null=False)
    followers_name = models.CharField(max_length=255, null=False)
    followers_bio = models.CharField(max_length=255, null=False)
    followers_location = models.CharField(max_length=255, null=False)

    def __str__(self):
        return 'follower: %s' % str(self.followers_acc)

class Following(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_followi', on_delete=models.CASCADE)
    following_acc = models.CharField(max_length=255, null=False)
    following_name = models.CharField(max_length=255, null=False)
    following_bio = models.CharField(max_length=255, null=False)
    following_location = models.CharField(max_length=255, null=False)

    def __str__(self):
        return 'followed: %s' % str(self.following_acc)

