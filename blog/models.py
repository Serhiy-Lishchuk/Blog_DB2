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


class Comments(models.Model):
    comments_post = models.ForeignKey(Post)
    comments = models.TextField()
    com_date = models.DateTimeField(auto_now_add=True)
    com_user = models.ForeignKey(User)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.comments

    def as_dict(self):
        items = {
            'comments_post': self.comments_post_id,
            'comments': self.comments_post,
            'com_data': self.com_date,
            'com_user': self.com_user
        }
        return items


class Reg(models.Model):
    reg_user = models.ForeignKey(User)
    fullname = models.CharField(max_length=100)
    birthday = models.CharField(max_length=20)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)

    class Meta:
        db_table = 'reg_user'

    def __str__(self):
        return self.reg_user

    def as_dict(self):
        items = {
            'reg_user': self.reg_user,
            'fullname': self.fullname,
            'birthday': self.birthday,
            'country': self.country,
            'city': self.city
        }
        return items
