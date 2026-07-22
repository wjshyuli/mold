from django.db import models

# Create your models here.



# 对应关系表，capsule 胶囊，specification规格 clamp 夹盘
class Correspondence(models.Model):
    capsule = models.CharField(max_length=30, verbose_name="胶囊",null=False, blank=False)
    clamp = models.CharField(max_length=30, verbose_name="夹盘",null=False, blank=False)
    specification = models.CharField(max_length=100, verbose_name="规格",null=False, blank=True,default="")
    priority = models.PositiveIntegerField(default=0, verbose_name="优先级",null=False, blank=False)
    backup1 = models.CharField(max_length=100, verbose_name="备用1", null=True, blank=True)
    backup2 = models.CharField(max_length=100, verbose_name="备用2", null=True, blank=True)
    backup3 = models.CharField(max_length=100, verbose_name="备用3", null=True, blank=True)

    update_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.capsule} - {self.specification}"


class Stock(models.Model):
    MachineStyle = models.CharField(verbose_name="机型", max_length=10,default="")
    Clamp = models.CharField(max_length=10, verbose_name="夹盘" ,default="")
    quantity = models.PositiveIntegerField(default=0, verbose_name="库存数")
    backup1 = models.PositiveIntegerField(default=0, verbose_name="备用1",null=True, blank=True)
    backup2 = models.PositiveIntegerField(default=0, verbose_name="备用2",null=True, blank=True)
    backup3 = models.PositiveIntegerField(default=0, verbose_name="备用3",null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.MachineStyle} | {self.MachineStyle}"

class Machine(models.Model):
    MachineStyle = models.CharField(verbose_name="机型", max_length=10,default="")
    MachineID = models.CharField(max_length=10, verbose_name="夹盘" ,default="")
    factory = models.PositiveIntegerField(default=0, verbose_name="库存数")
    backup1 = models.PositiveIntegerField(default=0, verbose_name="备用1")
    backup2 = models.PositiveIntegerField(default=0, verbose_name="备用2")
    backup3 = models.PositiveIntegerField(default=0, verbose_name="备用3")
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.MachineStyle} | {self.MachineStyle}"