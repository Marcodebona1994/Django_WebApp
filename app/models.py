from django.db import models


class BOP(models.Model):
    topn = models.IntegerField(default=20)
    DictSize = models.IntegerField(default=10)
    data = models.FileField(upload_to='uploads/')
    ppm = models.FileField(upload_to='uploads/')


class PLSA(models.Model):
    topic = models.IntegerField(default=5)
    topn = models.IntegerField(default=20)
    DictSize = models.IntegerField(default=10)
    data = models.FileField(upload_to='uploads/')
    ppm = models.FileField(upload_to='uploads/')
