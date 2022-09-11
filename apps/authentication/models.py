# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from common.methods import random_key_generator


# default methods here
def create_organization_key():
    return random_key_generator(size=10)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


# Create your models here.
class Organization(models.Model):
    org_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField(blank=True, null=True)
    org_key = models.TextField(default=create_organization_key)
    status = models.PositiveSmallIntegerField(default=2)
    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_date = models.DateField(auto_now=True, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'organization'


class User(AbstractBaseUser, PermissionsMixin):
    unique_code = models.CharField(max_length=12, null=True, blank=True)
    secret_token = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=254, blank=True, null=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    user_image = models.ImageField(upload_to='media/', default='media/no_image.png', null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    type = models.PositiveSmallIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    is_organization_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', null=True, blank=True, related_name="user_created_by_fk",
                                   on_delete=models.PROTECT)
    modified_by = models.ForeignKey('User', blank=True, related_name="user_modified_by_fk",
                                    null=True, on_delete=models.PROTECT)
    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    sort = models.CharField(max_length=20, null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=2, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name='user_organization_fk', null=True, blank=True,
                                     on_delete=models.PROTECT)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self):
        return self.email

    def __str__(self):
        return self.username
