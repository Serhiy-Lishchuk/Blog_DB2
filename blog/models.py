from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    content = models.ImageField()
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'publication'

    def __str__(self):
        return self.title

    def as_dict(self):
        items = {
            'author': self.author,
            'title': self.title,
            'text': self.text,
            'content': self.content,
            'likes': self.likes,
            'created_date': self.created_date
        }
        return items
