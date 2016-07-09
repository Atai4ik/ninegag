from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)
    date = models.DateTimeField()
    picture = models.ImageField(upload_to='post/post_picture/')
    text = models.TextField()
    display = models.BooleanField(default=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __unicode__(self):
        return self.title
