from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')


class Word(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    original_word = models.CharField(max_length=200)
    translate_word = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
