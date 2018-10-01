from django.contrib import admin

from .models import ActivityRecord


@admin.register(ActivityRecord)
class ActivityRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activityType', 'duration')
