from django.db import models


class Project(models.Model):#создали таблицу
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"