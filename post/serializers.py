from rest_framework import serializers
from .models import Category


serializers.ModelSerializer

class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True,
        max_length=30
        )
    slug = serializers.SlugField(required=False)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

