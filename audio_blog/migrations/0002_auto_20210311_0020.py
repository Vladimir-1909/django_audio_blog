# Generated by Django 3.1.7 on 2021-03-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='name',
            field=models.CharField(max_length=125, verbose_name='Название'),
        ),
    ]
