from django.urls import path, include
from .views import CategoryView, CategoryDetailView, TagView, TagDetailView, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<slug:pk>', CategoryDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<slug:pk>', TagDetailView.as_view()),
    # path('post/', PostViewSet.as_view({'get':'list', 'post':'create'})),
    # path('post/<int:pk>', PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'retrieve', 'delete':'destroy'}))
    path('', include(router.urls))
]