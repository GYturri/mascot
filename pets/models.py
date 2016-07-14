from __future__ import unicode_literals
from django.db import models
from usuarios.models import Usuario

class Pet(models.Model):
	name = models.CharField(max_length=50)
	birth = models.DateField('fecha de nacimiento de la mascota', auto_now_add=False)
	register = models.DateTimeField('fecha de registro', auto_now_add=True)
	photo = models.ImageField(upload_to='static/fotos/pets/', verbose_name=name, null=True, blank=True)
	estatus = models.BooleanField(default=True)#activo
	estate = models.BooleanField(default=False)#adoptado
	raza = models.CharField(max_length=50)#tipo de raza
	tipes = (
		('A', 'Perro'),
		('B', 'Gato'),
	)
	tipe = models.CharField(max_length=1, choices=tipes, default='A')
	sizes = (
		('A', 'Grande'),
		('B', 'Mediano'),
		('C', 'Peque'),
	)
	size = models.CharField(max_length=1, choices=sizes, default='A')
	observations = models.TextField(verbose_name='otros datos de importancia de la mascota', blank=True, null=True)
	country = models.CharField(max_length=50)
	region = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	usuario = models.ForeignKey(Usuario)
	def __str__(self):
		return '%s %s' % (self.name, self.tipe)
