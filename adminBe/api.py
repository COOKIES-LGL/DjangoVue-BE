# -*- coding: utf-8 -*-

# def get_all_category(request):
#     category = []
#     try:
#         result = LinkCategory.objects.all()
#     except ObjectDoesNotExist:
#         return JsonResponse({'status': 10023, 'message': '查询对象结果为空'})
#     # 给字典添加键值对
#     category = serializers.serialize('json', result)
#     return HttpResponse(category, content_type="application/json; charset=utf-8")

