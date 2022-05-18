from django.db import models
from django.urls import reverse


class TopicPhrase(models.Model):
    name = models.CharField('Тематика', max_length=200)
    translation = models.CharField('Перевод', max_length=100)
    url = models.SlugField(max_length=60, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


class Phrase(models.Model):
    text = models.CharField('Фраза', max_length=220)
    translation = models.CharField('Перевод', max_length=220)
    topic = models.ForeignKey(
        TopicPhrase, verbose_name='тематики', on_delete=models.SET_NULL, null=True, )
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('phrase_detail', kwargs={"slug": self.text})

    class Meta:

        verbose_name = "Фраза"
        verbose_name_plural = "Фразы"
