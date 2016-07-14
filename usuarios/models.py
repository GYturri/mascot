from __future__ import unicode_literals

# -*- coding: utf-8 -*-
from django.db import models
#para crear el nuevo modelo de usuario
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError('El email es oligatorio')
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, False, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=8, unique=True)
	email = models.EmailField(max_length=30, unique=True)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	seleccionsexo = (
		('A', 'masculino'),
		('B', 'femenino'),
	)
	sexo = models.CharField(max_length=1, choices=seleccionsexo, default='A')
	nacimiento = models.DateField('fecha de nacimiento', auto_now_add=False, null=True, blank=True)
	photo = models.ImageField(upload_to='static/fotos/usuarios/', verbose_name=username, null=True, blank=True)
	celular = models.CharField(max_length=9)
	direccion = models.CharField(max_length=200)
	create = models.DateTimeField('fecha de registro', auto_now_add=True)
	modified = models.DateTimeField('fecha de modificacion', auto_now_add=False, null=True, blank=True)
	
	objects = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.first_name