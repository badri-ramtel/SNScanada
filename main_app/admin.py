from django.contrib import admin
from main_app.models import Slider, President,PresidentMessage, Subscribe, Advertise, AlertMessage, AlertMessageHide
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
admin.site.register(AlertMessage)
admin.site.register(AlertMessageHide)