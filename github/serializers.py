# from rest_framework import serializers
from .models import *

# class GithuberSerializer(serializers.ModelSerializer):
#     owner_repo = serializers.StringRelatedField(many=True)
#     owner_star = serializers.StringRelatedField(many=True)
#     owner_follow = serializers.StringRelatedField(many=True)
#     owner_followi = serializers.StringRelatedField(many=True)
    

#     class Meta:
#         model = Githuber
#         fields = (
#             'useracc',
#             'username',
#             'bio',
#             'location',
#             'owner_repo',
#             'owner_star',
#             'owner_follow',
#             'owner_followi',
#         )
        # ordering = ['useracc']