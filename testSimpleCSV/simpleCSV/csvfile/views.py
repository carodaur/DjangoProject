import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Workschedule
from django.db import connection
from .models import sql_cursor
from .models import PayrollList
from django.views.generic.list import ListView
from django.utils import timezone
import datetime
from .models import ReportIDChecklist
from .models import checkReportID

# Create your views here.

# one parameter naemd request
def workschedule_upload(request):

    # declaring template
    template = "workschedule_upload.html"
    data = Workschedule.objects.all()
    payrolllist = PayrollList.objects.all()


    # prompt is a context variable that can have different
    # values depending on their context
    prompt = {
        'order': 'Order of the CSV should be date, hoursworked, employeeid, jobgroup',
        'Workschedules': data
    }

    # GET request returns the value of the data with the
    # specified key
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    # let's check if it it a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    # read data from the csv file
    data_set = csv_file.read().decode('UTF-8')

    # skip the last line of the data
    splited = data_set.split("report id", 1)
    # store all the data without last line into data_set
    data_set = splited[0]
    # extract the reportID from the last line
    reportID = int(splited[1].replace(',',''),10)
    ret = checkReportID(reportID)

    # declaring a template for displaying
    template_error = "Error_Reupload.html"
    if ret == False:
        return render(
            request,
            template_error,
            {'reportid':reportID,
            }
        )

    # setup a stream which is when we loop through each line
    # we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Workschedule.objects.update_or_create(
            date=datetime.datetime.strptime(column[0], "%d/%m/%Y").strftime("%Y-%m-%d"),
            hoursworked=column[1],
            employeeid=column[2],
            jobgroup=column[3]
        )
    context = {}

    # declaring a new template for displaying Payroll
    template_payroll = "payroll.html"

    employeeID, years, payment, answer = sql_cursor()


    return render(
            request,
            template_payroll,
            {'workschedules': data,
            'payrolllist': payrolllist,
            #'employeeID': employeeID,
            #'years': years,
            #'payment': payment,
            #'answer': answer,
            }
        )

'''
class PayrollListView(ListView):
    model = Payroll
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
'''
