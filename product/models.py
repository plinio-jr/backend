from distutils.command.upload import upload
from email.mime import image
from io import BytesIO
from tkinter import image_names
from unicodedata import category, decimal
from PIL import Image

from django.core.files import File
from django.db import models
from stripe import Price

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbanail(self.image)
                self.save()

                return  'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

class Mercado(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    avaliacao = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.nome

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    peso = models.DecimalField(max_digits=4, decimal_places=3)
    quantidade = models.DecimalField(max_digits=4, decimal_places=3)
    mercado = models.ForeignKey(
        Mercado, on_delete=models.PROTECT, related_name="products"
    )

    def __str__(self):
        return f"{self.nome} ({self.price})"

class Lista(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    produto = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="+")

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
   