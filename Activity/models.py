from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User


def get_default_user():
    return User.objects.get(id=1)


""" ActivityRecord consist of a type of activity and the duration of that activity"""
# todo: duration in hours and minutes
# todo: type you can choose from predefined list in dropdown menu
@python_2_unicode_compatible
class ActivityRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    activityType = models.CharField(max_length=300)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return "{0}   {1}   {2}".format(self.user, self.activityType, self.duration)

