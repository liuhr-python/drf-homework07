
from django.db import models

class Computer(models.Model):
    name = models.CharField(max_length=80, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=16, verbose_name="品牌")

    class Meta:
        db_table = 'computer_list'
        verbose_name = "电脑表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
