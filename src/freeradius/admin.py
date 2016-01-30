from django.contrib import admin
from freeradius.models import *

class BadUsersAdmin(admin.ModelAdmin):
    model = BadUsers

class NASAdmin(admin.ModelAdmin):
    model = NAS

class RadAcctAdmin(admin.ModelAdmin):
    model = RadAcct
    list_display = ('username', 'groupname', 'realm', 'nasipaddress', 'nasportid', 'acctstarttime',
    	'acctstoptime', 'acctsessiontime', 'acctinputoctets', 'acctoutputoctets', 'acctterminatecause')

class RadCheckAdmin(admin.ModelAdmin):
    model = RadCheck
    search_fields = ['username__username']
    list_display = ('username', 'attribute', 'op', 'value')

class RadGroupCheckAdmin(admin.ModelAdmin):
    model = RadGroupCheck

class RadGroupReplyAdmin(admin.ModelAdmin):
    model = RadGroupReply

class RadIPPoolAdmin(admin.ModelAdmin):
    model = RadIPPool

class RadPostAuthAdmin(admin.ModelAdmin):
    model = RadPostAuth

class RadReplyAdmin(admin.ModelAdmin):
    model = RadReply

class RadUserGroupAdmin(admin.ModelAdmin):
    model = RadUserGroup

class TotAcctAdmin(admin.ModelAdmin):
    model = TotAcct

class UserBillingDetailAdmin(admin.ModelAdmin):
    model = UserBillingDetail
    list_display = ('username', 'anniversary_day', 'action', 'status')

class UserDataAdmin(admin.ModelAdmin):
    model = UserData
    list_display = ('username', 'date', 'data_hour', 'tdata')

    def tdata(self, obj):
    	return "%sGB" % (obj.totaldata/1024/1024/1024);

class UserQuotaAdmin(admin.ModelAdmin):
    model = UserQuota
    list_display = ('username', 'quota_date', 'quota')

class UserStatsAdmin(admin.ModelAdmin):
    model = UserStats
    list_display = ('username', 'acctsessionid', 'timestamp', 'acctinputoctets', 'acctoutputoctets')

class UserInfoAdmin(admin.ModelAdmin):
    model = UserInfo
    search_fields = ['username', 'name']


admin.site.register(BadUsers, BadUsersAdmin)

admin.site.register(NAS, NASAdmin)

admin.site.register(RadAcct, RadAcctAdmin)

admin.site.register(RadCheck, RadCheckAdmin)

admin.site.register(RadGroupCheck, RadGroupCheckAdmin)

admin.site.register(RadGroupReply, RadGroupReplyAdmin)

admin.site.register(RadIPPool, RadIPPoolAdmin)

admin.site.register(RadPostAuth, RadPostAuthAdmin)

admin.site.register(RadReply, RadReplyAdmin)

admin.site.register(RadUserGroup, RadUserGroupAdmin)

admin.site.register(TotAcct, TotAcctAdmin)

admin.site.register(UserBillingDetail, UserBillingDetailAdmin)

admin.site.register(UserData, UserDataAdmin)

admin.site.register(UserQuota, UserQuotaAdmin)

admin.site.register(UserStats, UserStatsAdmin)

admin.site.register(UserInfo, UserInfoAdmin)
