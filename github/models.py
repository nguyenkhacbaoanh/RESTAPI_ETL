from django.db import models

# Create your models here.
class Githuber(models.Model):
    useracc = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False)
    bio = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '%s: %s' % (str(useracc), str(username))

class Repository(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_repo', on_delete=models.CASCADE)
    repo = models.CharField(max_length=255, null=False)
    used_lang = models.CharField(max_length=255, null=False)


class Star(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_star', on_delete=models.CASCADE)
    repo_starred = models.CharField(max_length=255, null=False)
    used_lang_starred = models.CharField(max_length=255, null=False)

class Follower(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_follow', on_delete=models.CASCADE)
    followers_acc = models.CharField(max_length=255, null=False)
    followers_name = models.CharField(max_length=255, null=False)
    followers_bio = models.CharField(max_length=255, null=False)
    followers_location = models.CharField(max_length=255, null=False)

class Following(models.Model):
    repo_owner = models.ForeignKey(Githuber, related_name='owner_followi', on_delete=models.CASCADE)
    following_acc = models.CharField(max_length=255, null=False)
    following_name = models.CharField(max_length=255, null=False)
    following_bio = models.CharField(max_length=255, null=False)
    following_location = models.CharField(max_length=255, null=False)

