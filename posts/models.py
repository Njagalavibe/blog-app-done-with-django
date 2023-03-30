from django.db import models


class Post(models.Model):
    Title = models.CharField(max_length=16,null=True)
    text = models.TextField()
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Title
        