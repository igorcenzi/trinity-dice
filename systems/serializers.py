from rest_framework import serializers
from django.shortcuts import get_object_or_404


from .models import System
# from classes.models import Class

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'
        read_only_fields = ['id', 'classes']
        depth = 1

