# Generated by Django 4.0.4 on 2022-05-16 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicPhrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тематика')),
                ('translation', models.CharField(max_length=100, verbose_name='Перевод')),
                ('url', models.SlugField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=220, verbose_name='Фраза')),
                ('translation', models.CharField(max_length=220, verbose_name='Перевод')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='phrasebook.topicphrase', verbose_name='тематики')),
            ],
            options={
                'verbose_name': 'Фраза',
                'verbose_name_plural': 'Фразы',
            },
        ),
    ]