# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_company_jd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='a_backlog',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='cgpa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='t_backlog',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='x',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='xii',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]