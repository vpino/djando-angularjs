from rest_framework import permissions


class IsAuthorOfPost(permissions.BasePermission):
	"""Funcion para validar si el usuario tiene permisos 
		para crear un nuevo POST

	"""
	def has_object_permission(self, request, view, post):
		if request.user:
			return post.author == request.user
		return False