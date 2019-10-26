from django.db import models
from django.conf import settings
from datetime import date
from django.db import connection


# Create your models here.
class Workschedule(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    hoursworked = models.DecimalField(max_digits=5, decimal_places=2)
    employeeid = models.IntegerField()
    jobgroup = models.CharField(max_length=1)

    def __str__(self):
        return self.date
    class Meta:
        db_table = "workschedule"
        #app_label = "workschedule"

class Payroll(models.Model):
    employeeid = models.IntegerField()
    payperiod = models.CharField(max_length=24)
    amountpaid = models.CharField(max_length=20)


def sql_cursor():
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT employeeid FROM workschedule ORDER BY employeeid ASC")
        employeeID = cursor.fetchall()
        workInfo = []
        salary = []
        monthPerID = []
        realmonthPerID = []
        hourse_jobgroup = []

        for eID in employeeID:
            # look for all the month for each ID
            cursor.execute("SELECT date FROM workschedule WHERE employeeid=%s", [eID[0]])
            monthPerIDEntry = cursor.fetchall()
            monthPerID.append(monthPerIDEntry)
            realMonthPer = []
            for monthDate in monthPerIDEntry:
                realMonth = monthDate[0].month
                realMonthPer.append(realMonth)
                realmonthPerID.append(realMonth)
                #cursor.execute("SELECT hoursworked, jobgroup FROM workschedule WHERE employeeid=%s AND date LIKE %s", [eID[0], '_____'+str(realMonth)+'%'])
                #hourse_jobgroup.append(cursor.fetchall())

            realMonthPer = remove_duplicate(realMonthPer)
            for realMonth in realMonthPer:
                cursor.execute("SELECT hoursworked, jobgroup FROM workschedule WHERE employeeid=%s AND date LIKE %s", [eID[0], '_____'+str(realMonth)+'%'])
                hourse_jobgroup.append(cursor.fetchall())

            # look for all the entries for each ID
            cursor.execute("SELECT date, hoursworked, jobgroup FROM workschedule WHERE employeeid=%s", [eID[0]])
            workInfoPerID = cursor.fetchall()
            hoursPerID = 0
            for perWork in workInfoPerID:
                hoursPerID += perWork[1]
            if workInfoPerID[0][2] == 'A':
                salary.append(hoursPerID * 20)
            else:
                salary.append(hoursPerID * 30)

            workInfo.append(workInfoPerID)

        cursor.execute("SELECT date FROM workschedule WHERE employeeid=%s AND date LIKE %s", ['4', '_____' + str(2) + '%'])
        answer = cursor.fetchall()


    return employeeID, workInfo, salary, monthPerID, realmonthPerID, hourse_jobgroup, answer

def remove_duplicate(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
