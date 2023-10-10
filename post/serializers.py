from rest_framework import serializers
from .models import Category, Tag, Post
from review.serializers import CommentSerializer
from django.db.models import Avg


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
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        tags = validated_data.pop('tags', [])
        post = self.Meta.model.objects.create(author=user, **validated_data)
        post.tags.add(*tags)
        return post

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['comment'] = CommentSerializer(instance.comments.all(), many=True).data
    #     return representation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating'] = instance.ratings.aggregate(Avg('rating'))['rating_avg']
        representation['comment'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['likes'] = instance.likes.count()
        return representation

    
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'id')



