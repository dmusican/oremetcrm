# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='family_name',
            field=models.CharField(default='MIGRATIONDEFAULT', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='family',
            name='address1',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='address2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='children',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='city',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='comments1',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='comments2',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='grandchildren',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='member_since',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='pets',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='state',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='contact_notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email1',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email2',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='executive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='jcs',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='leadership',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='newsletter_by_mail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone1',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone2',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
