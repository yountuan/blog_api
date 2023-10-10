from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Comment, Rating, Like
from rest_framework.exceptions import ValidationError


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        post = self.Meta.model.objects.create(author=user, **validated_data)
        return post


class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if rating > 10:
            raise ValidationError('Rating should be more than 10')
        return rating

    def create(self, validated_data):
        user = self.context.get('request').user
        rating = self.Meta.model.objects.create(author=user, **validated_data)
        return rating

    # def update(self, instance, validated_data):
    #     instance.rating = validated_data.get('rating')
    #     instance.save()
    #     return super().update(instance, validated_data)

    def validate(self, attrs):
        post = attrs.get('post')
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(post=post, author=user).exists():
            raise ValidationError('You already rated')
        return attrs


class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        like = self.Meta.model.objects.create(author=user, **validated_data)
        return like

