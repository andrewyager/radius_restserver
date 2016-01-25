from freeradius.models import UserData, UserBillingDetail, UserQuota, UserInfo
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ('username', 'datain', 'dataout', 'totaldata', 'data_hour', 'date')

class UserQuotaSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserQuota
		fields = ('username', 'quota_date', 'quota')

class UserBillingSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserBillingDetail
		fields = ('username', 'anniversary_day', 'action', 'status')

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserInfo
		fields = ('username', 'name', 'mail', 'department', 'workphone', 'homephone', 'mobile')