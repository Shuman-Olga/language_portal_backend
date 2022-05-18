from django.db import models
from django.urls import reverse


class TopicVideo(models.Model):
    name = models.CharField('Тематика', max_length=200)
    url = models.SlugField(max_length=60, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


class Video(models.Model):
    title = models.CharField('Название', max_length=100)
    videoid = models.CharField(max_length=120)
    url = models.SlugField(max_length=130, unique=True)
    topic = models.ForeignKey(
        TopicVideo, verbose_name='тематики', on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={"slug": self.text})

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
