from django.contrib import admin
from apps.models import AppModel, Comments, Issues, AppStats
# Register your models here.

admin.site.register(AppModel)
admin.site.register(Comments)
admin.site.register(Issues)
admin.site.register(AppStats)
