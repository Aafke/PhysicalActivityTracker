from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Activity.models import ActivityRecord


@login_required
def home(request):
    number_of_user_records = ActivityRecord.objects.activity_records_for_user(request.user).count()
    user_records = ActivityRecord.objects.activity_records_for_user(request.user)

    return render(request, "UserPage/home.html",
                  {'nrecords': number_of_user_records,
                   'records': user_records})
