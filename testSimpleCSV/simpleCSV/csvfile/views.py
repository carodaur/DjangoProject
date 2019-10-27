import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Workschedule
from django.db import connection
from .models import sql_cursor
from .models import Payroll

# Create your views here.

# one parameter naemd request
def workschedule_upload(request):

    # declaring template
    template = "workschedule_upload.html"
    data = Workschedule.objects.all()


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

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line
    # we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Workschedule.objects.update_or_create(
            date=column[0],
            hoursworked=column[1],
            employeeid=column[2],
            jobgroup=column[3]
        )
    context = {}

    # declaring a new template for displaying Payroll
    template_payroll = "payroll.html"

    employeeID, years, payment, answer = sql_cursor()

    payroll = Payroll.objects.all()


    return render(
            request,
            template_payroll,
            {'workschedules': data,
            'payrolls': payroll,
            'employeeID': employeeID,
            'years': years,
            'payment': payment,
            'answer': answer,
            }
        )
