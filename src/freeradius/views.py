from django.shortcuts import render

# Create your views here.
from .models import UserData
from .serializers import UserDataSerializer
from .permissions import IsCurrentUser
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

class UserDataList(mixins.ListModelMixin, generics.GenericAPIView):
	queryset = UserData.objects.all()
	serializer_class = UserDataSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			username = self.request.query_params.get('username', None)
			if username is not None:
				return UserData.objects.filter(username__username=username)
			else:
				return UserData.objects.all()
		return UserData.objects.filter(username__username=user.username)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

