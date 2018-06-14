import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# class Player(models.Model):
#     sex = models.CharField(max_length=10)
#     ages = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.sex


class Post(models.Model):
    profile_pic = models.ImageField(upload_to="blog/profile_pic")
    # 저장경로 : MEDIA_ROOT/blog/profile_pic/xxxx.jpg 경로에 저장
    # DB필드 : 'MEDIA_URL/blog/profile_pic/xxxx.jpg' 문자열 저장
    photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
# 저장경로 : MEDIA_ROOT/blog/2017/05/10/xxxx.jpg 경로에 저장
# DB필드 : 'MEDIA_URL/blog/2017/05/10/xxxx.jpg' 문자열 저장
