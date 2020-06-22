from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from transliterate import translit


class CategoryGroup(models.Model):
    cat_group_name = models.CharField(
        max_length=20,
        verbose_name="Группа товаров",
        null=False,
    )

    def __str__(self):
        return self.cat_group_name


class Category(models.Model):
    group = models.ForeignKey(
        CategoryGroup,
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_DEFAULT
    )
    cat_name = models.CharField(
        max_length=20,
        verbose_name="Категория товаров",
        null=False,
    )

    def __str__(self):
        return self.cat_name


class Merchandise(models.Model):
    category = models.ForeignKey(
        Category,
        null=False,
        default=0,
        on_delete=models.SET_DEFAULT
    )
    name = models.CharField(
        max_length=20,
        verbose_name="Название",
        null=False,
    )
    price = models.FloatField(
        null=False,
        verbose_name="Цена"
    )
    picture = models.ImageField(
        upload_to='./static/images/istore',
        verbose_name="Фото",
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.slug == '':
            self.slug = slugify(translit(self.name, reversed=True))
        super(Merchandise, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1, "★"
        TWO = 2, "★★"
        THREE = 3, "★★★"
        FOUR = 4, "★★★★"
        FIVE = 5, "★★★★★"

    product = models.ForeignKey(
        Merchandise,
        null=False,
        on_delete=models.CASCADE
    )
    author = models.CharField(
        max_length=20,
        verbose_name="Автор",
    )
    rating = models.IntegerField(
        default=Rating.FIVE,
        choices=Rating.choices,
        verbose_name='Оценка'
    )
    comment_text = models.TextField(
        verbose_name="Отзыв"
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.author}: {self.product}"


class Article(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        verbose_name="Название"
    )
    text = models.TextField(
        verbose_name="Текст"

    )
    merch = models.ManyToManyField(
        Merchandise,
        related_name="articles",
        verbose_name="Продукты"
    )

    creation_date = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=False
    )
    products = models.ManyToManyField(
        Merchandise,
        related_name='orders',
        through='OrderDetails',
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.user.email} {self.created.timestamp()}"


class OrderDetails(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Merchandise,
        on_delete=models.CASCADE
    )
    quantity = models.FloatField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return f"{self.order.user.username} {self.product.name}"
