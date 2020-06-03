from django.db import models

DEFAULT_LENGTH = 255

class Vendor(models.Model):
    name = models.CharField(
        max_length = DEFAULT_LENGTH,
        )

# Create your models here.
class Phone(models.Model):
    name = models.CharField(
        max_length = DEFAULT_LENGTH,
        verbose_name="Name"
        )
    vendor = models.ForeignKey(
        "Vendor",
        on_delete = models.SET_NULL,
        null = True,
        blank = True
        )
    price = models.FloatField()
    operating_system = models.CharField(
        max_length = DEFAULT_LENGTH,
        )
    ram = models.IntegerField()
    pixels = models.IntegerField()
    double_camera = models.BooleanField()
    processor = models.CharField(
        max_length = DEFAULT_LENGTH,
        )
    screen = models.CharField(
        max_length = DEFAULT_LENGTH,
        )
    fm_radio  = models.BooleanField()
    misc = models.CharField(
        max_length = DEFAULT_LENGTH,
        )
    def misc_as_list(self):
        return self.misc.split(',')

class Samsung_Phones(models.Model):
    vendor = models.ForeignKey(
        "Vendor",
        on_delete = models.SET_NULL,
        null = True,
        blank = True
        )
    sams_field = models.CharField(
        max_length = DEFAULT_LENGTH,
        )
 
class Apple_Phones(models.Model):
    vendor = models.ForeignKey(
        "Vendor",
        on_delete = models.SET_NULL,
        null = True,
        blank = True
        )
    appl_field = models.CharField(
        max_length = DEFAULT_LENGTH,
        )