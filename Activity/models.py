from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User


class ActivityRecordQuerySet(models.QuerySet):
    def activity_records_for_user(self, user):

        return self.filter(user=user)

""" ActivityRecord consist of a type of activity and the duration of that activity"""
# todo: duration in hours and minutes
# todo: type you can choose from predefined list in dropdown menu
@python_2_unicode_compatible
class ActivityRecord(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    activity_type = models.CharField(
        max_length=300,
        verbose_name="Type of Activity",
        help_text="Please enter the type of activity")
    duration = models.IntegerField(
        default=0,
        verbose_name="Duration of activity")
    duration = models.IntegerField()

    objects = ActivityRecordQuerySet.as_manager()

    def __str__(self):
        return "{0}   {1}   {2}".format(self.user, self.activity_type, self.duration)


