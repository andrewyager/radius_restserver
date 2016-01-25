from django.shortcuts import render

# Create your views here.
from .models import UserData, UserQuota
from .serializers import UserDataSerializer, UserQuotaSerializer
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
    username = self.request.query_params.get('username', None)
    fromdate = self.request.query_params.get('fromdate', None)
    todate = self.request.query_params.get('todate', None)

    if user.is_superuser:
      if username is not None and fromdate is not None and todate is not None:
        return UserData.objects.filter(username__username=username, date__range=[fromdate, todate])
      elif username is not None:
        return UserData.objects.filter(username__username=username)
      else:
        return UserData.objects.all()
    else:
      if fromdate is not None and todate is not None:
        return UserData.objects.filter(username__username=user.username, date__range=[fromdate, todate])
      else:
        return UserData.objects.filter(username__username=user.username)


  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

class UserQuotaList(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = UserQuota.objects.all()
  serializer_class = UserQuotaSerializer
  permission_classes = (permissions.IsAuthenticated, )

  def get_queryset(self):
    user = self.request.user
    username = self.request.query_params.get('username', None)
    fromdate = self.request.query_params.get('fromdate', None)
    todate = self.request.query_params.get('todate', None)

    if user.is_superuser:
      if username is not None and fromdate is not None and todate is not None:
        return UserQuota.objects.filter(username__username=username, date__range=[fromdate, todate])
      elif username is not None:
        return UserQuota.objects.filter(username__username=username)
      else:
        return UserQuota.objects.all()
    else:
      if fromdate is not None and todate is not None:
        return UserQuota.objects.filter(username__username=user.username, date__range=[fromdate, todate])
      else:
        return UserQuota.objects.filter(username__username=user.username)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)


