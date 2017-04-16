from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from member.models import MomoUser, RelationShip

admin.site.register(MomoUser)
admin.site.register(RelationShip)
TokenAdmin.raw_id_fields = ('user',)
