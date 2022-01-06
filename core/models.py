from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
import uuid


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email is must')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_shop = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=50, unique=True)
    is_shop = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class UserProfile(models.Model):

    email = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='userprofile_email',
        on_delete=models.CASCADE
    )
    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(null=True)
    address_prefecture = models.CharField(max_length=10)
    address_city = models.CharField(max_length=20)
    hear_from = models.CharField(max_length=30)
    introduced = models.CharField(max_length=40, null=True)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.family_name + self.first_name


class UserInfo(models.Model):

    email = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='userinfo_email',
        on_delete=models.CASCADE
    )
    point = models.IntegerField(default=0)
    visit_count = models.IntegerField(default=0)
    continuous_visit_count = models.IntegerField(default=0)
    previous_visit = models.DateTimeField(null=True)
    last_visit = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.email)


class VisitHistory(models.Model):

    email = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='visit_history_email',
        on_delete=models.CASCADE
    )
    visited_date = models.DateTimeField(primary_key=True)

    def __str__(self):
        return str(self.email + self.visited_date)