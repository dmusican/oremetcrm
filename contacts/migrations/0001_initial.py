# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('grandchildren', models.TextField()),
                ('pets', models.TextField()),
                ('comments1', models.TextField()),
                ('comments2', models.TextField()),
                ('children', models.TextField()),
                ('member_since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=30)),
                ('phone2', models.CharField(max_length=30)),
                ('contact_notes', models.TextField()),
                ('executive', models.BooleanField()),
                ('leadership', models.BooleanField()),
                ('jcs', models.BooleanField()),
                ('status', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Member'), (b'V', b'Visitor'), (b'R', b'Removed')])),
                ('newsletter_by_mail', models.BooleanField()),
                ('family', models.ForeignKey(to='contacts.Family')),
            ],
        ),
    ]
