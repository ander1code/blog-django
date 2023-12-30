#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import *

class frmPost(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=None, required=False)
    title = forms.CharField(error_messages={
                             'required': 'Title is empty.', 'max_length': 'Title has more than 70 characters long.'})
    briefing = forms.CharField(error_messages={
                               'required': 'Briefing is empty.', 'max_length': 'Briefing has more than 100 characters.'})
    text = forms.CharField(error_messages={
                            'required': 'Text is empty.', 'max_length': 'Text has more than 3000 characters.'})
    image = forms.ImageField(error_messages={'required': 'Image wasn\'t selected.'})
    createDate = forms.DateTimeField(required=False)
    updateDate = forms.DateTimeField(required=False)

    class Meta:
        model = Post
        fields = "__all__"
