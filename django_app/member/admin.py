from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from member.models import MomoUser, RelationShip


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email', 'profile_img', 'date_joined', 'last_login', 'followers',
                    'following', 'is_facebook', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ['id', 'username', 'email', 'date_joined', 'last_login', 'is_facebook', 'is_superuser', 'is_active']
    list_select_related = True
    list_per_page = 100
    list_max_show_all = 200
    # list_editable = ()
    search_fields = ['username', 'email']


class RelationAdmin(admin.ModelAdmin):
    list_filter = ['to_user', 'from_user', 'created_date']
    search_fields = ['to_user', 'from_user']


admin.site.register(MomoUser, UserAdmin)
admin.site.register(RelationShip, RelationAdmin)
TokenAdmin.list_display = ('key', 'user', 'created')
TokenAdmin.fields = ('user',)
TokenAdmin.list_select_related = True
