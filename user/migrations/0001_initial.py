# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-12 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('password', models.CharField(max_length=150, verbose_name='密码')),
                ('tel', models.IntegerField(verbose_name='电话号码')),
                ('address', models.CharField(max_length=150, verbose_name='地址')),
                ('email', models.EmailField(max_length=60, verbose_name='邮箱')),
                ('category', models.CharField(max_length=30, verbose_name='用户类别')),
                ('avatar', models.ImageField(max_length=200, null=True, upload_to='avatar/', verbose_name='头像')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
