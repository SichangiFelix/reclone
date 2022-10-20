from pyexpat import model
from rest_framework import serializers
from .models import Post
from .models import Vote


# Create serializers for each model
#post
class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = 'poster.username')
    poster_id = serializers.ReadOnlyField(source = 'poster.id')
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster','poster_id', 'created']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']