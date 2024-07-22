from django.contrib import admin
from main_app.models import Slider, President,PresidentMessage, Subscribe, Advertise
from import_export.admin import ExportMixin

# Register your models here.
admin.site.register(Slider)
admin.site.register(President)
admin.site.register(PresidentMessage)

class SubscribeAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['email']
    actions = ["take_action"]
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Advertise)