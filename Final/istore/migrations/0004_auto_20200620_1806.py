# Generated by Django 3.0.7 on 2020-06-20 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('istore', '0003_category_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=5,
                                      verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='group',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT,
                                    to='istore.CategoryGroup'),
        ),
    ]
