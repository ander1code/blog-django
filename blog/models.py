#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=70, null=False)
    briefing = models.CharField(max_length=100, null=False)
    text = models.TextField(max_length=3000, null=False)
    image = models.ImageField(upload_to='post', blank=True, null=True, default='noimage.png')
    createDate = models.DateTimeField('Create Date', null=False)
    updateDate = models.DateTimeField('Update Date', null=True)

    def __unicode__(self):
        title = self.title
        return "%s - %s - %s" % (title[0:15], self.author, self.createDate)
    
    class Meta:
        verbose_name_plural = "Posts"