from dataclasses import field
from itertools import product
from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import Category, Lista, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = (
            "id",
             "name",
             "get_absolute_url",
             "description",
             "price",
             "get_image",
             "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = (
            "id",
             "nome",
             "descricao",
             "product",
        )

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = (
            "id",
             "nome",
             "rua",
             "bairro",
             "cidade",
        )