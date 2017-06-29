#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import  *

class frmBlog(forms.ModelForm):
    #autor = forms.IntegerField(error_messages={'required': 'Autor está vazio.'})
    titulo = forms.CharField(error_messages={'required': 'Titulo está vazio.', 'max_length':'Título esta com mais de 50 caracteres.' })
    briefing = forms.CharField(error_messages={'required': 'Briefing esta vazio.', 'max_length':'Briefing esta com mais de 50 caracteres.'})
    texto = forms.CharField(error_messages={'required': 'Texto esta vazio.', 'max_length':'Titulo esta com mais de 1400 caracteres.'})
    dataCriacao = forms.CharField(error_messages={'required': 'Data de criacao vazia.'})
    imagem = forms.ImageField(error_messages={'required': 'Image está vazia.'})
    dataCriacao.widget.attrs['readonly'] = True

    class Meta:
        model = Postagem
        fields = "__all__" 
