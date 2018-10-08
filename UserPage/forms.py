from django.forms import ModelForm

from Activity.models import ActivityRecord

class RecordEntryForm(ModelForm):
    class Meta:
        model= ActivityRecord
        exclude = ('user',)
