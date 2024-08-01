from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from contact_app.models import FeedBack, FeedbackInstruction, Member, MemberInstruction, MemberType, Vacancy, VacancyInstruction, Donation, DonationInstruction, DonationType
from import_export.admin import ExportActionMixin

# Register your models here.   
class FeedBackAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['full_name', 'email', 'address', 'contact', 'status']
    actions = ["take_action"]

    def take_action(self, request, queryset):
        updated = queryset.update(status="R")
        self.message_user(
            request, 
            ngettext(
                "%d Feedback was successfully marked as Read.",
                "%d Feedbacks were successfully marked as Read.",
                updated,
            )
            % updated,
            messages.SUCCESS, 
        )

admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(FeedbackInstruction)

class MemberAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'contact', 'address1', 'status']
    actions = ["take_action"]

    def take_action(self, request, queryset):
        updated = queryset.update(status="C")
        self.message_user(
            request, 
            ngettext(
                "%d Member was successfully marked as Confirmed.",
                "%d Members were successfully marked as Confirmed.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

admin.site.register(Member,MemberAdmin)
admin.site.register(MemberInstruction)
admin.site.register(MemberType)
admin.site.register(Vacancy)
admin.site.register(VacancyInstruction)

class DonationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'contact', 'address_1', 'country', 'donation_type', 'status']
    actions = ["take_action"]

    def take_action(self, request, queryset):
        updated = queryset.update(status="C")
        self.message_user(
            request, 
            ngettext(
                "%d Donation was successfully marked as Confirmed.",
                "%d Donations were successfully marked as Confirmed.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

admin.site.register(Donation, DonationAdmin)
admin.site.register(DonationInstruction)
admin.site.register(DonationType)