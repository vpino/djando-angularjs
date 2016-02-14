# -*- coding: utf-8 -*-

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.permissions import IsAuthorOfPost
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.order_by('-created_at')
	serializer_class = PostSerializer

	def get_permissions(self):
		
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAuthorOfPost(),)


	def perform_create(self, serializer):
		"""
		perform_create se llama antes de que se guarda el modelo de este punto de vista.

		Nosotros simplemente agarrar el usuario asociado 
		a esta solicitud y les hacemos el autor de este post.
		"""
		instance = serializer.save(author=self.request.user)

		return super(PostViewSet, self).perform_create(serializer)



class AccountPostsViewSet(viewsets.ViewSet):
	"""
	Este viewset se utiliza para mostrar los mensajes asociados a una cuenta específica.
	
	"""
	queryset = Post.objects.select_related('author').all()
	serializer_class = PostSerializer

	def list(self, request, account_username=None):
		
		queryset = self.queryset.filter(author__username=account_username)
		serializer = self.serializer_class(queryset, many=True)

	
		return Response(serializer.data)
