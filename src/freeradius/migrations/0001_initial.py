# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, null=True, db_column='UserName', blank=True)),
                ('date', models.DateTimeField(db_column='Date')),
                ('reason', models.CharField(max_length=200, null=True, db_column='Reason', blank=True)),
                ('admin', models.CharField(max_length=30, null=True, db_column='Admin', blank=True)),
            ],
            options={
                'db_table': 'badusers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NAS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nasname', models.CharField(max_length=128)),
                ('shortname', models.CharField(max_length=32, null=True, blank=True)),
                ('type', models.CharField(max_length=30, null=True, blank=True)),
                ('ports', models.IntegerField(null=True, blank=True)),
                ('secret', models.CharField(max_length=60)),
                ('community', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('server', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'db_table': 'nas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadAcct',
            fields=[
                ('radacctid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('acctsessionid', models.CharField(max_length=64)),
                ('acctuniqueid', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=64, db_column='UserName')),
                ('groupname', models.CharField(max_length=64, db_column='GroupName', blank=True)),
                ('realm', models.CharField(max_length=64, null=True, blank=True)),
                ('nasipaddress', models.CharField(max_length=15, db_column='NASIPAddress')),
                ('nasportid', models.CharField(max_length=15, null=True, db_column='NASPortId', blank=True)),
                ('nasporttype', models.CharField(max_length=32, null=True, blank=True)),
                ('acctstarttime', models.DateTimeField(null=True, db_column='AcctStartTime', blank=True)),
                ('acctstoptime', models.DateTimeField(null=True, db_column='AcctStopTime', blank=True)),
                ('acctsessiontime', models.IntegerField(null=True, db_column='AcctSessionTime', blank=True)),
                ('acctauthentic', models.CharField(max_length=32, null=True, blank=True)),
                ('connectinfo_start', models.CharField(max_length=50, null=True, blank=True)),
                ('connectinfo_stop', models.CharField(max_length=50, null=True, blank=True)),
                ('acctinputoctets', models.BigIntegerField(null=True, db_column='AcctInputOctets', blank=True)),
                ('acctoutputoctets', models.BigIntegerField(null=True, db_column='AcctOutputOctets', blank=True)),
                ('calledstationid', models.CharField(max_length=50, db_column='CalledStationId')),
                ('callingstationid', models.CharField(max_length=50, db_column='CallingStationId')),
                ('acctterminatecause', models.CharField(max_length=32)),
                ('servicetype', models.CharField(max_length=32, null=True, blank=True)),
                ('framedprotocol', models.CharField(max_length=32, null=True, blank=True)),
                ('framedipaddress', models.CharField(max_length=15, db_column='FramedIPAddress')),
                ('acctstartdelay', models.IntegerField(null=True, blank=True)),
                ('acctstopdelay', models.IntegerField(null=True, blank=True)),
                ('xascendsessionsvrkey', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'radacct',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=32)),
                ('op', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radcheck',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadGroupCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=32)),
                ('op', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radgroupcheck',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadGroupReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=32)),
                ('op', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radgroupreply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadIPPool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pool_name', models.CharField(max_length=30)),
                ('framedipaddress', models.CharField(max_length=15)),
                ('nasipaddress', models.CharField(max_length=15)),
                ('calledstationid', models.CharField(max_length=30)),
                ('callingstationid', models.CharField(max_length=30)),
                ('expiry_time', models.DateTimeField(null=True, blank=True)),
                ('username', models.CharField(max_length=64)),
                ('pool_key', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'radippool',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadPostAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('pass_field', models.CharField(max_length=64, db_column='pass')),
                ('reply', models.CharField(max_length=32)),
                ('authdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'radpostauth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=32)),
                ('op', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radreply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadUserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('groupname', models.CharField(max_length=64)),
                ('priority', models.IntegerField()),
            ],
            options={
                'db_table': 'radusergroup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotAcct',
            fields=[
                ('totacctid', models.BigIntegerField(serialize=False, primary_key=True, db_column='TotAcctId')),
                ('username', models.CharField(max_length=64, db_column='UserName')),
                ('acctdate', models.DateField(db_column='AcctDate')),
                ('connnum', models.BigIntegerField(null=True, db_column='ConnNum', blank=True)),
                ('conntotduration', models.BigIntegerField(null=True, db_column='ConnTotDuration', blank=True)),
                ('connmaxduration', models.BigIntegerField(null=True, db_column='ConnMaxDuration', blank=True)),
                ('connminduration', models.BigIntegerField(null=True, db_column='ConnMinDuration', blank=True)),
                ('inputoctets', models.BigIntegerField(null=True, db_column='InputOctets', blank=True)),
                ('outputoctets', models.BigIntegerField(null=True, db_column='OutputOctets', blank=True)),
                ('nasipaddress', models.CharField(max_length=15, null=True, db_column='NASIPAddress', blank=True)),
            ],
            options={
                'db_table': 'totacct',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserBillingDetail',
            fields=[
                ('username', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('anniversary_day', models.IntegerField()),
                ('action', models.CharField(max_length=6)),
                ('status', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'user_billing_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('datain', models.BigIntegerField()),
                ('dataout', models.BigIntegerField()),
                ('totaldata', models.BigIntegerField()),
                ('data_hour', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'user_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200, null=True, db_column='UserName', blank=True)),
                ('name', models.CharField(max_length=200, null=True, db_column='Name', blank=True)),
                ('mail', models.CharField(max_length=200, null=True, db_column='Mail', blank=True)),
                ('department', models.CharField(max_length=200, null=True, db_column='Department', blank=True)),
                ('workphone', models.CharField(max_length=200, null=True, db_column='WorkPhone', blank=True)),
                ('homephone', models.CharField(max_length=200, null=True, db_column='HomePhone', blank=True)),
                ('mobile', models.CharField(max_length=200, null=True, db_column='Mobile', blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'userinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserQuota',
            fields=[
                ('username', models.CharField(max_length=255)),
                ('quota_date', models.DateTimeField()),
                ('quota', models.BigIntegerField()),
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'user_quota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radacct_id', models.IntegerField()),
                ('username', models.CharField(max_length=64)),
                ('acctsessionid', models.CharField(max_length=64)),
                ('acctuniqueid', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField()),
                ('acctinputoctets', models.BigIntegerField()),
                ('acctoutputoctets', models.BigIntegerField()),
            ],
            options={
                'db_table': 'user_stats',
                'managed': False,
            },
        ),
    ]
