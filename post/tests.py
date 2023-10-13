from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import PostViewSet
from .models import Post, Category, Tag
from django.contrib.auth import get_user_model
from collections import OrderedDict
from rest_framework.utils.serializer_helpers import ReturnList
from django.urls import reverse
from rest_framework.authtoken.models import Token


class PostTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title='cat1')
        tag = Tag.objects.create(title='tag1')
        self.tags = [tag]
        self.user = get_user_model().objects.create_user(
            email='test_user@gmail.com', 
            password='12345',
            is_active=True, 
            name='test'
            )
        posts = [
            Post(
                author=self.user, body='first',
                title='post1', category=self.category
            ),            
            Post(
                author=self.user, body='second',
                title='post2', category=self.category
            ),             
            Post(
                author=self.user, body='third',
                title='post3', category=self.category
            ),
        ]
        Post.objects.bulk_create(posts)

    def authentification(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token: {self.token}')

    def test_list(self):
        request = self.factory.get('posts/')
        view = PostViewSet.as_view({'get': 'list'})
        response = view(request)
        # print('0000000000000000')
        # print(response, response.data)
        # assert response.status_code == 200
        print(type(response.data))
        assert type(response.data) == OrderedDict

    def test_retrieve(self):
        post = Post.objects.create(title='test', body='test', category=self.category, author=get_user_model().objects.get(email='test_user@gmail.com'))
        url = reverse('post-detail', kwargs={'pk': post.id})
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create(self):
        data = {
            'title': 'test-create', 'body': 'blabbla', 'category': self.category, 'author': self.user
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('post-list')
        response = self.client.post(url, data)
        assert Post.objects.get(title='test-create').body == data['body']

    def test_update(self):
        post = Post.objects.create(title='test', body='test', category=self.category, author=get_user_model().objects.get(email='test_user@gmail.com'))
        url = reverse('post-detail', kwargs={'pk': post.id})
        data = {'title': 'test update', 'body': 'update', 'category': self.category}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        assert response.status_code == 200
