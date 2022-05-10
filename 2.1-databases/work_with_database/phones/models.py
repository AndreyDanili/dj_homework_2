from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1024)
    price = models.IntegerField()
    release_date = models.CharField(max_length=255)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, default='')

    # def __str__(self):
    #     return f'{self.name}, {self.image}, {self.price}, {self.release_date}, {self.lte_exists}, {self.slug}'
