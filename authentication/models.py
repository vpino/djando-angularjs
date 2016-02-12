from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
	""" Clase para Definir la estructura de un Usuario

    El motivo de crear esta clase es para editar la cuenta del usuario que se logueara
    en el sistema a nuestro gusto, debido a que la clase User de Django viene con 
    limitaciones

	"""

	email = models.EmailField(unique=True)

	username = models.CharField(max_length=40, unique=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=140, blank=True)
	tagline = models.CharField(max_length=140, blank=True)

	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	"""
		Funcion para cuando impriman un objeto de la clase
		Account les retorne el email
	"""
	def __unicode__(self):
		"""Funcion que retorna un string cuando se imprime una instancia del objeto

		Returns:
			String: Retorna el campo email de la clase

        """
		return self.email

	
	def get_full_name(self):
		"""Funcion que retorna el nombre completo del Usuario

		Returns:
			String: Retorna el campo first_name concatenado con el
					campo last_name

		"""
		return ''.join([self.first_name, self.last_name])


	def get_short_name(self):
		"""Funcion que retorna el primer nombre del Usuario

		Returns:
			String: Retorna el campo first_name 

		"""
        return self.first_name



