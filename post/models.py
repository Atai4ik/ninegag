# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)
    category = models.ForeignKey(Categories, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='post/post_picture/')
    text = models.TextField()
    display = models.BooleanField(default=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    class Meta:
        verbose_name = u'пост'
        verbose_name_plural = u'посты'
        ordering = ['-date']

    def __unicode__(self):
        return self.title
