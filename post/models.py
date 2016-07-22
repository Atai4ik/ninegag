# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from redactor.fields import RedactorField


class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название')
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название')
    slug = models.SlugField(max_length=30, unique=True)
    category = models.ForeignKey(Categories, blank=True, null=True, verbose_name=u'Категория')
    date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата')
    picture = models.ImageField(upload_to='post/post_picture/', verbose_name=u'Картинка')
    text = RedactorField(verbose_name=u'Текст')
    display = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        verbose_name = u'пост'
        verbose_name_plural = u'посты'
        ordering = ['-date']

    def __unicode__(self):
        return self.title



