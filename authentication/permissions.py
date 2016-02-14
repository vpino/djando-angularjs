# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
	"""
		Este es un permiso bastante básico. Si hay un usuario asociado con la petición actual, 
		comprobamos si el usuario es el mismo objeto que account. Si no hay ningún usuario asociado 
		a esta solicitud, simplemente retornamos Falso.
	"""
	def has_object_permission(self, request, view, account):
		if request.user:
			return account == request.user

		return False