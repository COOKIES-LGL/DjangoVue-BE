# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Categoryserializer, Linkserializer
from .models import LinkCategory
from .models import LinkList
from .models import SpecialCategory
from .models import SpecialLink
from django.http import QueryDict
from rest_framework.request import Request


def get_parameter_dic(request, *args, **kwargs):
    # 获取不同请求方式的参数
    if isinstance(request, Request) == False:
        return {}

    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data


class RestfulCategoryView(APIView):
    def get(self, request, format=None):
        data = LinkCategory.objects.all().order_by('order_id')
        serializer = Categoryserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Categoryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RestfulSpecialCategoryView(APIView):
    def get(self, request, format=None):
        data = SpecialCategory.objects.all()
        serializer = Linkserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Linkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RestfulGetCategoryByType(APIView):
    def get(self, request, format=None):
        serializer = request.query_params
        print (serializer['category_type'])
        type = serializer['category_type']
        data = LinkCategory.objects.filter(category_type=type) # category_type为1面经，为2时为工具
        serializer = Categoryserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Linkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RestfulGetLinksByIds(APIView):
    def get(self, request, format=None):
        serializer = request.query_params
        lv1 = serializer['lv1']
        lv2 = serializer['lv2']
        data = LinkList.objects.filter(parent_id=lv2, grandparent_id=lv1).order_by('order_id')
        serializer = Linkserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        params = get_parameter_dic(request)
        print (params)
        for item in request.data.linkList:
            serializer = Linkserializer(data=item)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RestfulAddLinks(APIView):
    def get(self, request, format=None):
        serializer = request.query_params
        lv1 = serializer['grandparent_id']
        data = LinkList.objects.filter(grandparent_id=lv1)
        serializer = Linkserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Linkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RestfulGetLinksById(APIView):
    def get(self, request, format=None):
        serializer = request.query_params
        lv1 = serializer['grandparent_id']
        data = LinkList.objects.filter(grandparent_id=lv1)
        serializer = Linkserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Linkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RestfulGetSpecialLinksById(APIView):
    def get(self, request, format=None):
        serializer = request.query_params
        lv1 = serializer['parent_id']
        data = SpecialLink.objects.filter(parent_id=lv1)
        serializer = Linkserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Linkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
