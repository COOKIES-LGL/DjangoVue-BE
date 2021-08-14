from django.contrib import admin
from adminBe.models import AdminUserInfo, Article, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, DjangoAdminLog
from adminBe.models import DjangoContentType, DjangoMigrations, DjangoSession, LinkCategory, LinkList, UserInfo, SpecialLink, SpecialCategory


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'password', 'create_time', 'user_level', 'user_email']


admin.site.register(UserInfo, UserInfoAdmin)


class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'session_data', 'expire_date']


admin.site.register(DjangoSession, DjangoSessionAdmin)


class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ['object_id', 'action_time', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user']


admin.site.register(DjangoAdminLog, DjangoAdminLogAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'article_title', 'article_create_time', 'article_status', 'article_category', 'article_sub_category', 'article_author']


admin.site.register(Article, ArticleAdmin)


class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'category_level', 'category_parent', 'order_id', 'category_type']


admin.site.register(LinkCategory, LinkCategoryAdmin)


class LinkListAdmin(admin.ModelAdmin):
    list_display = ['id', 'link_title', 'create_time', 'parent_id', 'grandparent_id', 'link_desc', 'view_count',
                    'link_status', 'link_type', 'link_loves', 'link_need_vpn', 'order_id']


admin.site.register(LinkList, LinkListAdmin)


class SpecialLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'link_title', 'create_time', 'parent_id', 'grandparent_id', 'link_desc', 'view_count',
                    'link_status', 'link_type', 'link_loves', 'link_need_vpn', 'order_id']


admin.site.register(SpecialLink, SpecialLinkAdmin)


class SpecialCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_level', 'category_parent', 'order_id']


admin.site.register(SpecialCategory, SpecialCategoryAdmin)
# Register your models here.


