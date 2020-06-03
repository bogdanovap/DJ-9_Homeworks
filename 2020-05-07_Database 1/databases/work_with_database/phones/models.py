from django.db import models
from django.utils.text import slugify

DEFAULT_LENGTH = 255

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(
        max_length = DEFAULT_LENGTH,
        )
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(
        max_length = DEFAULT_LENGTH,
        )
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
