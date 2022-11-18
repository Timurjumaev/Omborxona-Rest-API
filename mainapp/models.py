from django.contrib.auth.models import User
from django.db import models


class Sotuvchi(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    manzil = models.CharField(max_length=60)
    tel = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism}, {self.nom}, {self.manzil}"

class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    narx=models.IntegerField()
    miqdor=models.IntegerField()
    brend=models.CharField(max_length=50)
    kelgan_sana=models.DateField(auto_now_add=True)
    olchov=models.CharField(max_length=50)
    sotuvchi=models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.nom}, {self.brend}"

class Mijoz(models.Model):
    ism=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    manzil=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    qarz=models.IntegerField(default=0)
    sotuvchi=models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.ism}, {self.nom}({self.manzil})"

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.FloatField()
    sana = models.DateTimeField(auto_now=True)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    jami = models.FloatField()
    tolandi = models.FloatField()
    nasiya = models.IntegerField()
    def __str__(self): return self.mahsulot.nom

