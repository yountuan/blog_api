from rest_framework import serializers
from .models import Category, Tag, Post


serializers.ModelSerializer

# class CategorySerializer(serializers.Serializer):
#     title = serializers.CharField(
#         required=True,
#         max_length=30
#         )
#     slug = serializers.SlugField(required=False)

#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'id')

