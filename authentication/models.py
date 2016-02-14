# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
    	""" Clase para crear un usuario

	   
	    Args:
      	  param1 (email): El email del usuario
      	  param2 (str): La contraseña del usuario
      	  **kwargs: Arbitrary keyword arguments.
       
        Returns:
          account: retoruna un objeto de la clase Account


        Raises:
      		
      	  ValueError: Si `param1` no es un correo valido.
      				  Si `**kwargs` nombre de usuario no es valido.
		"""
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
    	""" Clase para convertir un usuario normal a super usuario

	   
	    Args:
      	  param1 (email): El email del usuario
      	  param2 (str): La contraseña del usuario
      	  **kwargs: Arbitrary keyword arguments.
       
        Returns:
          account: retoruna un objeto de la clase Account

      	"""
      		
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
	""" Clase para Definir la estructura de un Usuario

    El motivo de crear esta clase es para editar la cuenta del usuario que se logueara
    en el sistema a nuestro gusto, debido a que la clase User de Django viene con 
    limitaciones

    Los campos con el atributo blank=True seran campos opcionales
	"""


	email = models.EmailField(unique=True)

	username = models.CharField(max_length=40, unique=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=140, blank=True)
	tagline = models.CharField(max_length=140, blank=True)

	is_admin = models.BooleanField(default=False)

	"""
	El campo created_at registra el momento en el que se crea la cuenta. Con la aprobación 
	de auto_now_add = True a models.DateTimeField, le estamos diciendo a Django que este 
	campo debe establecerse de forma automática cuando se crea el objeto y no se 
	puede editar después de eso.
	"""

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()

	"""
	Para agregar un nuevo usuario, django requiere un nombre de usuario. El nombre de usuario se utiliza para 
	iniciar la sesión del usuario. Por el contrario, nuestra aplicación utilizará la dirección de 
	correo electrónico del usuario para este propósito.

	USERNAME_FIELD = 'email'

	"""

	USERNAME_FIELD = 'email'

	"""
	Como este modelo es la sustitución del modelo de usuario
	Django nos obliga a especificar los campos requeridos de esta manera.
	REQUIRED_FIELDS = ['username']

	"""
	REQUIRED_FIELDS = ['username']

	
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






