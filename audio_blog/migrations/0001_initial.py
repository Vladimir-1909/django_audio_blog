# Generated by Django 3.1.7 on 2021-03-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Жанр')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('audio', models.FileField(upload_to='music/')),
                ('genres', models.ManyToManyField(blank=True, related_name='posts', to='audio_blog.Genre')),
            ],
            options={
                'verbose_name': 'Аудио',
                'verbose_name_plural': 'Аудио',
            },
        ),
    ]
