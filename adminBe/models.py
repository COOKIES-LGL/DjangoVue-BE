# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
#   * python manage.py inspectdb > adminBe/models.py 注释admin的引入
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdminUserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    user_level = models.IntegerField()
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'admin_user_info'


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100)
    article_content = models.TextField()
    article_create_time = models.DateTimeField()
    article_update_time = models.DateTimeField(blank=True, null=True)
    article_status = models.IntegerField()
    article_category = models.CharField(max_length=100)
    article_sub_category = models.CharField(max_length=100)
    article_author = models.CharField(max_length=100)
    article_keywords = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LinkCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_level = models.IntegerField()
    category_parent = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.IntegerField()
    category_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_category'


class LinkList(models.Model):
    link_title = models.CharField(max_length=100)
    create_time = models.BigIntegerField(blank=True, null=True)
    link_icon = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField()
    grandparent_id = models.IntegerField(blank=True, null=True)
    link_desc = models.CharField(max_length=100)
    view_count = models.IntegerField(blank=True, null=True)
    link_loves = models.IntegerField(blank=True, null=True)
    link_type = models.IntegerField()
    link_status = models.IntegerField()
    link_need_vpn = models.IntegerField()
    order_id = models.IntegerField(blank=True, null=True)
    link_url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'link_list'


class SpecialCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_level = models.IntegerField()
    category_parent = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.IntegerField()
    category_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'special_category'


class SpecialLink(models.Model):
    link_title = models.CharField(max_length=100)
    create_time = models.BigIntegerField(blank=True, null=True)
    link_icon = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField()
    grandparent_id = models.IntegerField(blank=True, null=True)
    link_desc = models.CharField(max_length=100)
    view_count = models.IntegerField(blank=True, null=True)
    link_loves = models.IntegerField(blank=True, null=True)
    link_type = models.IntegerField()
    link_status = models.IntegerField()
    link_need_vpn = models.IntegerField()
    order_id = models.IntegerField(blank=True, null=True)
    link_url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'special_link'


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    user_level = models.IntegerField()
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_info'
