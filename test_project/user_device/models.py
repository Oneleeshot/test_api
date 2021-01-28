import pdb

from PIL import Image
from django.db import models


class Workers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True,
                              default='media/123.png')
    company = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Device(models.Model):
    device = models.CharField(max_length=255)
    configuration = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    paid_by = models.CharField(max_length=50, blank=True)
    used_by = models.ForeignKey(Workers, on_delete=models.SET_DEFAULT,
                                default=None, null=True, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()

    def __str__(self):
        return self.device
