from rest_framework.viewsets import ModelViewSet
from .models import Comment, Rating, Like
from .serializers import CommentSerializer, RatingSerializer, LikeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAuthor
from rest_framework import generics


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()


class LikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
