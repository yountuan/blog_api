from django.urls import path, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]


# TODO: to_representation 
# приложение аккаунта

