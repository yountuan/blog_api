from django.urls import path, include
from .views import CommentViewSet, RatingViewSet, LikeView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('likes/', LikeView.as_view())
]


# TODO: to_representation 
# приложение аккаунта

