from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    text = models.TextField(verbose_name="内容")
    date_added = models.DateTimeField(default=timezone.now, verbose_name="发布日期")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.title[:50]}... (作者: {self.owner.username})"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogs:index')