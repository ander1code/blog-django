#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        error_messages={
            'null': 'Author is required.',
            'invalid': 'Invalid author.',
        }
    )

    title = models.CharField(
        'Title',
        max_length=70,
        null=False,
        blank=False,
        error_messages={
            'blank': 'Title is required.',
            'null': 'Title cannot be null.',
            'max_length': 'Title must be at most 70 characters.',
        },
        validators=[
            MinLengthValidator(5, message="Title must be at least 5 characters."),
            MaxLengthValidator(70, message="Title must be at most 70 characters."),
        ]
    )

    briefing = models.CharField(
        'Briefing',
        max_length=100,
        null=False,
        blank=False,
        error_messages={
            'blank': 'Briefing is required.',
            'null': 'Briefing cannot be null.',
            'max_length': 'Briefing must be at most 100 characters.',
        },
        validators=[
            MinLengthValidator(5, message="Briefing must be at least 5 characters."),
            MaxLengthValidator(100, message="Briefing must be at most 100 characters."),
        ]
    )

    text = models.TextField(
        'Text',
        null=False,
        blank=False,
        error_messages={
            'blank': 'Text is required.',
            'null': 'Text cannot be null.',
        },
        validators=[
            MinLengthValidator(100, message="Text must be at least 100 characters."),
            MaxLengthValidator(3000, message="Text must be at most 3000 characters."),
        ]
    )

    picture = models.ImageField(
        "Picture",
        upload_to='posts/',
        default='posts/noimage.png',
        error_messages={
            'blank': 'Picture is empty.',
            'null': 'Picture is null.',
            'invalid': 'Invalid picture file.'
        }
    )

    create_at = models.DateTimeField(
        'Create At',
        default=timezone.now,
        null=False,
        blank=False,
        error_messages={
            'blank': 'Creation date is required.',
            'null': 'Creation date cannot be null.',
            'invalid': 'Invalid datetime format for creation date.',
        }
    )

    update_at = models.DateTimeField(
        'Update At',
        null=True,
        blank=True,
        error_messages={
            'invalid': 'Invalid datetime format for update date.',
        }
    )

    def clean(self):
        super().clean()
        if self.update_at and self.update_at < self.create_at:
            raise ValidationError({
                'update_at': 'Update date cannot be earlier than creation date.'
            })

    def __str__(self):
        return f"{self.title[:15]} - {self.author.username} - {self.create_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
