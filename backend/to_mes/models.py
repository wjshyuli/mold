from django.db import models

# Create your models here.



# 对应关系表，capsule 胶囊，specification规格 clamp 夹盘
class Correspondence(models.Model):
    capsule = models.CharField(max_length=30, verbose_name="胶囊")
    specification = models.CharField(max_length=100, verbose_name="规格")
    clamp = models.CharField(max_length=30, verbose_name="夹盘")
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.capsule} - {self.specification}"


class Stock(models.Model):
    type = models.CharField(verbose_name="类型", max_length=5)
    specification = models.CharField(max_length=30, unique=True, verbose_name="规格")
    quantity = models.PositiveIntegerField(default=0, verbose_name="库存数量")


    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.type} | {self.type}"