from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response


class CategoryView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CategorySerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
