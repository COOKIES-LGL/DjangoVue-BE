"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.conf.urls import url
from views import RestfulCategoryView, RestfulGetLinksByIds, RestfulSpecialCategoryView, RestfulGetLinksById, \
    RestfulGetCategoryByType, RestfulAddLinks, RestfulGetSpecialLinksById

urlpatterns = [
    url(r'^getAllCategory/', RestfulCategoryView.as_view(), name='getAllCategory'),
    url(r'^getLinksById/', RestfulGetLinksById.as_view(), name='getLinksById'),
    url(r'^orderLinksByIds/', RestfulGetLinksByIds.as_view(), name='orderLinksByIds'),
    url(r'^editLinks/', RestfulAddLinks.as_view(), name='editLinks'),
    url(r'^getLinksByIds/', RestfulGetLinksByIds.as_view(), name='getLinksByIds'),
    url(r'^getCategoryByType/', RestfulGetCategoryByType.as_view(), name='getCategoryByType'),
    url(r'^getSpecialCategory/', RestfulSpecialCategoryView.as_view(), name='getSpecialCategory'),
    url(r'^getSpecialLinksById/', RestfulGetSpecialLinksById.as_view(), name='getSpecialLinksById'),
]
