from freeradius.models import UserData, UserBillingDetail, UserQuota, UserInfo
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ('username', 'datain', 'dataout', 'totaldata', 'data_hour', 'date')