from django.db import models
from django.urls import reverse


class TopicWord(models.Model):
    name = models.CharField('Тематика', max_length=200)
    translation = models.CharField('Перевод', max_length=100)
    image = models.ImageField("Изображение", upload_to="media/img/")
    url = models.SlugField(max_length=60, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


class Word(models.Model):
    word = models.CharField('Слово', max_length=150)
    transcription = models.CharField('Транскрипция', max_length=150)
    translation = models.CharField('Перевод', max_length=150)
    topic = models.ForeignKey(
        TopicWord, verbose_name='тематики', on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('phrase_detail', kwargs={"slug": self.text})

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
