from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from member.models import MomoUser

admin.site.register(MomoUser)
TokenAdmin.raw_id_fields = ('user',)
