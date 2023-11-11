# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import LinkCategory
from .models import LinkList


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = LinkCategory      #指定数据库
        fields = "__all__"         #拿到数据库所有字段信息，但只是这个数据库数据，拿不到关联数据库信息

    #     user_type=serializers.CharField(source='get_user_type_dispaly')
    #     role = serializers.CharField(source='role.title')
    #     group = serializers.SerializerMethodField(source='group.all')  #自定义显示
    #     fields=['id','user_type','role','group']

    # def get_group(self,row):                       #自定义方法，可选择关联表需要显示的信息
    #     group_obj_list=row.all()
    #     ret=[]
    #     for item in group_obj_list:
    #         ret.append({"id":item.id,"title":item.title})
    #     return ret
    #
    # def to_representation(self, obj):
    #     """将从 Model 取出的数据 parse 给 Api"""
    #     return obj
    #
    # def to_internal_value(self, data):
    #     """将客户端传来的 json 数据 parse 给 Model"""
    #     return json.loads(data.encode(‘utf - 8‘))


class Linkserializer(serializers.ModelSerializer):
    class Meta:
        model = LinkList  # 指定数据库
        fields = "__all__"  # 拿到数据库所有字段信息，但只是这个数据库数据，拿不到关联数据库信息
