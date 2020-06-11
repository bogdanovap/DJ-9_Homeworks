from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()


class Review(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Машина'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название статьи',
    )
    text = models.TextField(
        verbose_name='Статья',
    )

    def __str__(self):
        return str(self.car) + ' ' + self.title

