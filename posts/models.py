from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    url = models.URLField()
    user = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Post #{self.id} - {self.title}'


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'

    def __str__(self):
        return f'Vote #{self.id} by {self.user} on {self.post}'
