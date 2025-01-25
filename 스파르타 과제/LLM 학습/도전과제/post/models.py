# post/models.py
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=200, verbose_name="레시피 제목")
    ingredients = models.TextField(verbose_name="재료")
    instructions = models.TextField(verbose_name="조리순서")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "레시피"
        verbose_name_plural = "레시피 목록"

    def __str__(self):
        return self.title
