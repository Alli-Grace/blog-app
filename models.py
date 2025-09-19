# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.contrib.auth.base_user import BaseUserManager

# class CustomBaseManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email = email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff being set True")
        
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser being set True")

#         return self.create_user(email=email, password=password, **extra_fields)


# class CustomUser(AbstractUser):
#     is_admin = models.BooleanField(default=False)
#     is_member = models.BooleanField(default=False)

#     username = None
#     email = models.EmailField(unique=True)

#     groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permission', blank=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomBaseManager()

#     def __str__(self):
#         return self.first_name



# from django.db import models
# from datetime import datetime
# from main.models import CustomUser
# # Create your models here.
# class Post(models.Model):
#     # creator = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='')
#     title = models.CharField(max_length=100)
#     body = models.CharField(max_length=100000)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)

# # class Comment(models.Model):
# #     commentor = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='commentors')
# #     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
# #     text = models.CharField(max_length=500)