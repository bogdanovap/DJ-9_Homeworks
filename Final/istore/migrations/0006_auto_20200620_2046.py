# Generated by Django 3.0.7 on 2020-06-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('istore', '0005_merchandise_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creation_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=5,
                                      verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='./static/images/istore', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
