# Generated by Django 3.0.7 on 2020-06-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('istore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='picture',
            field=models.ImageField(blank=True, null=True,
                                    upload_to='F:\\Work\\Netology\\DJ-9\\Final\\istore\\static\\images',
                                    verbose_name='Фото'),
        ),
    ]
