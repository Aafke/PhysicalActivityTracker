from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Activity.models import ActivityRecord
from .forms import RecordEntryForm


@login_required
def home(request):
    number_of_user_records = ActivityRecord.objects.activity_records_for_user(request.user).count()
    user_records = ActivityRecord.objects.activity_records_for_user(request.user)

    return render(request, "UserPage/home.html",
                  {'nrecords': number_of_user_records,
                   'records': user_records})


@login_required
def new_activity_record(request):
    if request.method == "POST":
        record = ActivityRecord(user=request.user)
        form = RecordEntryForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('UserPage_home')
    else:
        form = RecordEntryForm()
    return render(request, "UserPage/new_activity_record_form.html", {'form': form})
