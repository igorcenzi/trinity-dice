from django.db import IntegrityError
from django.test import TestCase
from users.models import User

class UserModelTest(TestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    cls.username = 'Jorginho'
    cls.email = 'jorginho_joga_10@gmail.com'
    cls.password = '123@456'
    cls.phone = '+55212345678'
    cls.is_master = False
    
    cls.user = User.objects.create_user(
      username = cls.username, 
      email = cls.email, 
      password = cls.password, 
      phone = cls.phone, 
      is_master = cls.is_master
    )
    
  def test_should_create_user(self):
    self.assertTrue(hasattr(self.user, 'id'))
    self.assertTrue(hasattr(self.user, 'username'))
    self.assertTrue(hasattr(self.user, 'email'))
    self.assertTrue(hasattr(self.user, 'phone'))
    self.assertTrue(hasattr(self.user, 'is_master'))
    self.assertTrue(hasattr(self.user, 'is_active'))
    self.assertTrue(hasattr(self.user, 'created_at'))
    self.assertTrue(hasattr(self.user, 'updated_at'))
  
  def test_should_not_create_duplicated_username(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        username = self.username,
        email = "new_email@mail.com",
        password = self.password,
        phone = self.phone,
        is_master = self.is_master
      )
      
  def test_should_not_create_duplicated_email(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        username = "another_user",
        email = self.email,
        password = self.password,
        phone = self.phone,
        is_master = self.is_master
      )
  
  def test_should_not_create_without_email(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        username = self.username,
        password = self.password,
        phone = self.phone,
        is_master = self.is_master
      )
      
  def test_should_not_create_without_username(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        email = self.email,
        password = self.password,
        phone = self.phone,
        is_master = self.is_master
      )
      
  def test_should_not_create_without_password(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        username = self.username,
        email = self.email,
        phone = self.phone,
        is_master = self.is_master
      )
      
  def test_should_not_create_without_phone(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        username = self.username,
        email = self.email,
        password = self.password,
        is_master = self.is_master
      )
      
  def test_should_not_create_without_is_master(self):
    with self.assertRaises(IntegrityError):
      User.objects.create(
        username = self.username,
        email = self.email,
        password = self.password,
        phone = self.phone
      )
      
  