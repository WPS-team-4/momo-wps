from django.contrib import admin
<<<<<<< HEAD
=======
from rest_framework.authtoken.admin import TokenAdmin
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039

from member.models import MomoUser

admin.site.register(MomoUser)
<<<<<<< HEAD
=======
TokenAdmin.raw_id_fields = ('user',)
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
