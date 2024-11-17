from rest_framework import serializers
from .models import *

class qu(serializers.ModelSerializer):
    class Meta:
        model = quote
        fields = ['quote','author']
class auther(serializers.ModelSerializer):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)