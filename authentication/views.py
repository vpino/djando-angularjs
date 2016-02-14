# -*- coding: utf-8 -*-
from rest_framework import permissions, viewsets

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer
import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import status, views, permissions
from rest_framework.response import Response


class AccountViewSet(viewsets.ModelViewSet):
	"""

	lookup_field: Atributo por cual atributo buscaramos a los usuarios
				  en este caso no sera por el ID si no por el username

	queryset: Query que ejecutaremos

	serializer_class = Clase que se va a serializar

	"""

	lookup_field = 'username'
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get_permissions(self):

		#Verificamos si el usuario tiene permisos
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		#Verificamos que el metodo por donde se enviaron los datos sea POST
		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)


	def create(self, request):

		"""Funcion para crear un usuario con una contraseña codificada

		Metodo que sustituye .create() por Account.objects.create_user

		"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Account.objects.create_user(**serializer.validated_data)

			return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

		return Response({
		'status': 'Bad request',
		'message': 'Account could not be created with received data.'
		}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
	"""Clase para loguear en el sistema

	"""
	
	def post(self, request, format=None):
		data = json.loads(request.body)

		email = data.get('email', None)
		password = data.get('password', None)

		account = authenticate(email=email, password=password)

		if account is not None:
			if account.is_active:
				#creamos una nueva sesion para el usuario
				login(request, account)

				#serializamos el usuario
				serialized = AccountSerializer(account)

				#lo retornamos como un json
				return Response(serialized.data)
			
			else:
				
				return Response({
					'status': 'Unauthorized',
					'message': 'This account has been disabled.'
				}, status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response({
				'status': 'Unauthorized',
				'message': 'Username/password combination invalid.'
			}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutView(views.APIView):
	
	"""
	Clase para cerrar sesion

	"""

	#validamos que el usuario este logueado, si no le mando un error 403
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request, format=None):

		#SI el usuario esta logueado, cerramos la sesion
	    logout(request)

	    #No hay nada razonable para volver al salir,
	    #por lo que sólo devuelve una respuesta vacía con un código de estado 200.
	    return Response({}, status=status.HTTP_204_NO_CONTENT)