#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Postagem(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=100)
    briefing = models.CharField(max_length=50)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='media', blank=True, null=True, default='noimage.png')
    dataCriacao = models.DateTimeField('Data da Criacao')

    def __unicode__(self):
        titulo = self.titulo
        return "%s - %s - %s" % (titulo[0:15], self.autor, self.dataCriacao)

