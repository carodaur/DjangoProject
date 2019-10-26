from django import forms
from .models import Workschedule

class WorkscheduleForm(forms.ModelForm):

    class Meta:
        model = Workschedule
        fields = ['date', 'hoursworked', 'employeeid', 'jobgroup']

    date = forms.DateField(
        #widget=forms.DateInput(formate=)
        #attrs={'class': 'Workschedule'},
        input_formats=('%d/%m/%Y', )
        )
