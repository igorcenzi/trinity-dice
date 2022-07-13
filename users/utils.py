from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
  
  def _create_user(self, username, email, password, is_master, is_superuser, **extra_fields):
    email = self.normalize_email(email)
    
    user = self.model(
      username=username,
      email = email,
      is_master=is_master,
      is_superuser = is_superuser,
      **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    
    return user
  
  
  def create_superuser(self, username, email, password, is_master, **extra_fields):
    return self._create_user(username, email, password, is_master, True, **extra_fields)
  
  def create_user(self, username, email, password, is_master, **extra_fields):
    return self._create_user(username, email, password, is_master, False, **extra_fields)
    