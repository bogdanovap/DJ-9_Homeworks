# Generated by Django 2.2.10 on 2020-06-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200605_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', through='articles.ArticleTags', to='articles.Article'),
        ),
    ]
