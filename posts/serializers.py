from pyexpat import model
from rest_framework import serializers
from .models import Post
from .models import Vote


# Create serializers for each model
#post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'poster', 'created']

