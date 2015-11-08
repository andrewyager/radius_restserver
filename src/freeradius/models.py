# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BadUsers(models.Model):
    username = models.CharField(db_column='UserName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=200, blank=True, null=True)  # Field name made lowercase.
    admin = models.CharField(db_column='Admin', max_length=30, blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.username+" "+self.date+" "+self.reason

    class Meta:
        managed = False
        db_table = 'badusers'


class NAS(models.Model):
    nasname = models.CharField(max_length=128)
    shortname = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    ports = models.IntegerField(blank=True, null=True)
    secret = models.CharField(max_length=60)
    community = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    server = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return self.shortname+" ("+self.nasname+")"

    class Meta:
        managed = False
        db_table = 'nas'


class RadAcct(models.Model):
    radacctid = models.BigIntegerField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(max_length=32)
    username = models.CharField(db_column='UserName', max_length=64)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=64)  # Field name made lowercase.
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasipaddress = models.CharField(db_column='NASIPAddress', max_length=15)  # Field name made lowercase.
    nasportid = models.CharField(db_column='NASPortId', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nasporttype = models.CharField(max_length=32, blank=True, null=True)
    acctstarttime = models.DateTimeField(db_column='AcctStartTime', blank=True, null=True)  # Field name made lowercase.
    acctstoptime = models.DateTimeField(db_column='AcctStopTime', blank=True, null=True)  # Field name made lowercase.
    acctsessiontime = models.IntegerField(db_column='AcctSessionTime', blank=True, null=True)  # Field name made lowercase.
    acctauthentic = models.CharField(max_length=32, blank=True, null=True)
    connectinfo_start = models.CharField(max_length=50, blank=True, null=True)
    connectinfo_stop = models.CharField(max_length=50, blank=True, null=True)
    acctinputoctets = models.BigIntegerField(db_column='AcctInputOctets', blank=True, null=True)  # Field name made lowercase.
    acctoutputoctets = models.BigIntegerField(db_column='AcctOutputOctets', blank=True, null=True)  # Field name made lowercase.
    calledstationid = models.CharField(db_column='CalledStationId', max_length=50)  # Field name made lowercase.
    callingstationid = models.CharField(db_column='CallingStationId', max_length=50)  # Field name made lowercase.
    acctterminatecause = models.CharField(max_length=32)
    servicetype = models.CharField(max_length=32, blank=True, null=True)
    framedprotocol = models.CharField(max_length=32, blank=True, null=True)
    framedipaddress = models.CharField(db_column='FramedIPAddress', max_length=15)  # Field name made lowercase.
    acctstartdelay = models.IntegerField(blank=True, null=True)
    acctstopdelay = models.IntegerField(blank=True, null=True)
    xascendsessionsvrkey = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radacct'


class RadCheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=32)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    def __unicode__(self):
        return self.username+" "+self.attribute+self.op+self.value

    class Meta:
        managed = False
        db_table = 'radcheck'


class RadGroupCheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=32)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    def __unicode__(self):
        return self.groupname+" "+self.attribute+self.op+self.value

    class Meta:
        managed = False
        db_table = 'radgroupcheck'


class RadGroupReply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=32)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    def __unicode__(self):
        return self.groupname+" "+self.attribute+self.op+self.value

    class Meta:
        managed = False
        db_table = 'radgroupreply'


class RadIPPool(models.Model):
    pool_name = models.CharField(max_length=30)
    framedipaddress = models.CharField(max_length=15)
    nasipaddress = models.CharField(max_length=15)
    calledstationid = models.CharField(max_length=30)
    callingstationid = models.CharField(max_length=30)
    expiry_time = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=64)
    pool_key = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'radippool'


class RadPostAuth(models.Model):
    username = models.CharField(max_length=64)
    pass_field = models.CharField(db_column='pass', max_length=64)  # Field renamed because it was a Python reserved word.
    reply = models.CharField(max_length=32)
    authdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radpostauth'


class RadReply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=32)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    def __unicode__(self):
        return self.username+" "+self.attribute+self.op+self.value


    class Meta:
        managed = False
        db_table = 'radreply'


class RadUserGroup(models.Model):
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    priority = models.IntegerField()

    def __unicode__(self):
        return self.username+" "+self.groupname


    class Meta:
        managed = False
        db_table = 'radusergroup'


class TotAcct(models.Model):
    totacctid = models.BigIntegerField(db_column='TotAcctId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=64)  # Field name made lowercase.
    acctdate = models.DateField(db_column='AcctDate')  # Field name made lowercase.
    connnum = models.BigIntegerField(db_column='ConnNum', blank=True, null=True)  # Field name made lowercase.
    conntotduration = models.BigIntegerField(db_column='ConnTotDuration', blank=True, null=True)  # Field name made lowercase.
    connmaxduration = models.BigIntegerField(db_column='ConnMaxDuration', blank=True, null=True)  # Field name made lowercase.
    connminduration = models.BigIntegerField(db_column='ConnMinDuration', blank=True, null=True)  # Field name made lowercase.
    inputoctets = models.BigIntegerField(db_column='InputOctets', blank=True, null=True)  # Field name made lowercase.
    outputoctets = models.BigIntegerField(db_column='OutputOctets', blank=True, null=True)  # Field name made lowercase.
    nasipaddress = models.CharField(db_column='NASIPAddress', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'totacct'


class UserBillingDetail(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    anniversary_day = models.IntegerField()
    action = models.CharField(max_length=6)
    status = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'user_billing_detail'


class UserData(models.Model):
    username = models.CharField(max_length=255)
    datain = models.BigIntegerField()
    dataout = models.BigIntegerField()
    totaldata = models.BigIntegerField()
    data_hour = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'user_data'
        unique_together = (('username', 'data_hour', 'date'),)


class UserQuota(models.Model):
    username = models.CharField(max_length=255)
    quota_date = models.DateTimeField()
    quota = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_quota'


class UserStats(models.Model):
    radacct_id = models.IntegerField()
    username = models.CharField(max_length=64)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    acctinputoctets = models.BigIntegerField()
    acctoutputoctets = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_stats'


class UserInfo(models.Model):
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=200, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=200, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'
