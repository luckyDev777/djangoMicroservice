from rest_framework import serializers
from .models import Post, Category
import requests
from rest_framework.exceptions import ValidationError
from .tasks import publish_event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'category', 'category_id', 'author_id']
    
    def get_author(self, obj):
        user_service_url = f'http://user-service:8000/users/{obj.author_id}/'
        response = requests.get(user_service_url)
        if response.status_code == 200:
            return response.json()
        return None
    
    def validate_author_id(self, value):
        user_service_url = f'http://user-service:8000/users/{value}/'
        response = requests.get(user_service_url)
        if response.status_code == 404:
            raise ValidationError(f"User with {value} does not exists")
        return value
    
    def create(self, validated_data):
        post = super().create(validated_data)
        event_data = {
            'post_id': post.id,
            'title': post.title,
            'content': post.content,
            'author_id': post.author_id,
            'category_id': post.category_id
        }
        publish_event('post.created', event_data)
        return post
