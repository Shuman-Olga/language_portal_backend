from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField('Название', max_length=100)
    videoid = models.CharField(max_length=120)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    sub_en = models.TextField('Sub_en')
    sub_ru = models.TextField('Sub_ru')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
