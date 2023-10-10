from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import Category, Tag, Post
from .serializers import CategorySerializer, TagSerializer, PostSerializer, PostListSerializer
from rest_framework.response import Response



# class CategoryView(APIView):
#     def get(self, request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data, status=200)

#     def post(self, request):
#         serializer = CategorySerializer(
#             data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = [IsAdminUser]

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         self.permission_classes = [IsAdminUser]
    #     else:
    #         self.permission_classes = [AllowAny]
    #     return super().permission_classes()



class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # def get_permissions(self):
    #     if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
    #         self.permission_classes = [IsAdminUser]
    #     else:
    #         self.permission_classes = [AllowAny]
    #     return super().permission_classes()


class PostSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [OrderingFilter, SearchFilter]
#     ordering_fields = ['title']
#     search_fields = ['title']
#     pagination_class = PostSetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title']
    pagination_class = PostSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return self.serializer_class

    