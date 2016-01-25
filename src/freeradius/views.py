from django.shortcuts import render

# Create your views here.
from .models import UserData, UserQuota, UserInfo, UserBillingDetail
from .serializers import UserDataSerializer, UserQuotaSerializer, UserInfoSerializer, UserBillingSerializer
from .permissions import IsCurrentUser
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics, permissions
from rest_framework.response import Response


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

class UserInfoList(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = UserInfo.objects.all()
  serializer_class = UserQuotaSerializer
  permission_classes = (permissions.IsAuthenticated, )

  def get_queryset(self):
    user = self.request.user
    username = self.request.query_params.get('username', None)

    if user.is_superuser:
      if username is not None:
        return UserInfo.objects.filter(username__username=username)
      else:
        return UserInfo.objects.all()
    else:
      return UserInfo.objects.filter(username__username=user.username)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

class UserInfoList(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = UserInfo.objects.all()
  serializer_class = UserInfoSerializer
  permission_classes = (permissions.IsAuthenticated, )

  def get_queryset(self):
    user = self.request.user
    username = self.request.query_params.get('username', None)

    if user.is_superuser:
      if username is not None:
        return UserInfo.objects.filter(username=username)
      else:
        return UserInfo.objects.all()
    else:
      return UserInfo.objects.filter(username=user.username)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

class UserBillingDetailList(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = UserBillingDetail.objects.all()
  serializer_class = UserBillingSerializer
  permission_classes = (permissions.IsAuthenticated, )

  def get_queryset(self):
    user = self.request.user
    username = self.request.query_params.get('username', None)

    if user.is_superuser:
      if username is not None:
        return UserBillingDetail.objects.filter(username__username=username)
      else:
        return UserBillingDetail.objects.all()
    else:
      return UserBillingDetail.objects.filter(username__username=user.username)
  
  def get_object(self):
    user = self.request.user

    return UserBillingDetail.objects.get(username__username=user.username)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)


class QuotaDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
  permission_classes = (permissions.IsAuthenticated, )

  def get_queryset(self):
    user = self.request.user
    username = self.request.query_params.get('username', None)

    if user.is_superuser:
      if username is not None:
        return UserBillingDetail.objects.filter(username__username=username)
      else:
        return UserBillingDetail.objects.all()
    else:
      return UserBillingDetail.objects.filter(username__username=user.username)

  def get(self, request, username=None, period=0, *args, **kwargs):
    import sys
    print >>sys.stderr, username
    if username==None:
        username = self.request.user

    user = get_object_or_404(self.get_queryset(), username__username=username)
    return Response(user.get_quota_usage(int(period)))

    
