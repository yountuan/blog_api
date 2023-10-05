from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} {self.body} {self.post.title}'
    
