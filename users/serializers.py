from datetime import datetime
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only = True)
  created_at = serializers.DateTimeField(default=datetime.now())
  updated_at = serializers.DateTimeField(default=datetime.now())
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email', 'is_master', 'phone', 'created_at', 'updated_at', 'is_active']
    read_only_fields = ['id', 'created_at', 'updated_at', 'is_active']
    
  def create(self, validated_data: dict) -> User:
    user = User.objects.create_user(**validated_data)
    return user
  
  def update(self, instance: User, validated_data: dict) -> User:
    password = False
    if validated_data['is_master']:
      raise ValidationError({
   "detail": "Can't edit field is_master" 
 })
    if validated_data.get('password'):
      password = validated_data.pop('password')
    if validated_data.get('email') == instance.email:
      validated_data.pop('email')
    if validated_data.get('username') == instance.username:
      validated_data.pop('username')
    for key, value in validated_data.items():
      setattr(instance, key, value)
    if password:
      instance.set_password(password)
    instance.save()
    return instance