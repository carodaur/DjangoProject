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


class PayrollList(models.Model):
    employeeid = models.IntegerField()
    payperiod = models.CharField(max_length=24)
    amountpaid = models.CharField(max_length=10)

    def __str__(self):
        return self.employeeid
    class Meta:
        db_table = "payrolllist"


class ReportIDChecklist(models.Model):
    reportid = models.IntegerField()

    def __str__(self):
        return self.reportid
    class Meta:
        db_table = "reportidchecklist"

def sql_cursor():
    with connection.cursor() as cursor:

        cursor.execute("DELETE FROM payrolllist")

        # look for all employees
        cursor.execute("SELECT DISTINCT employeeid FROM workschedule ORDER BY employeeid ASC")
        employeeID = cursor.fetchall()


        years = []
        payment = []

        # for each employee, do analysis
        for eID in employeeID:
            # look for all the months for each ID
            cursor.execute("SELECT date FROM workschedule WHERE employeeid=%s", [eID[0]])
            dateEntries = cursor.fetchall()
            months = []
            realDayPer = []
            # go to each entry of with different dates to extract the months
            for dateEntry in dateEntries:
                month = dateEntry[0].month
                months.append(month)

                years.append(dateEntry[0].year)


            years = remove_duplicate(years)
            years.sort()
            # look for tasks in yearly order
            for year in years:
                # look for all tasks in each month
                months = remove_duplicate(months)
                for month in months:
                    cursor.execute("SELECT date, hoursworked, jobgroup FROM workschedule WHERE employeeid=%s AND date LIKE %s",
                                [eID[0], str(year)+'-%'+str(month)+'%-%']
                            )
                    entries = cursor.fetchall()
                    firstHalf = 0
                    secondHalf = 0
                    for entry in entries:
                        day = entry[0].day
                        hours = entry[1]
                        jobType = entry[2]
                        if day <= 15:
                            if jobType == 'A':
                                firstHalf += hours * 20
                            if jobType == 'B':
                                firstHalf += hours * 30
                        else:
                            if jobType == 'A':
                                secondHalf += hours * 20
                            if jobType == 'B':
                                secondHalf += hours * 30

                    payment.append(firstHalf)
                    payment.append(secondHalf)

                    if firstHalf > 0:
                        cursor.execute("INSERT INTO payrolllist (employeeid, payperiod, amountpaid) VALUES (%s, %s, %s)",
                                    [eID[0], str(1)+'/'+str(month)+'/'+str(year)+' - '+str(15)+'/'+str(month)+'/'+str(year), '$'+str(firstHalf)]
                                )
                    if secondHalf > 0:
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                            cursor.execute("INSERT INTO payrolllist (employeeid, payperiod, amountpaid) VALUES (%s, %s, %s)",
                                        [eID[0], str(16)+'/'+str(month)+'/'+str(year)+' - '+str(31)+'/'+str(month)+'/'+str(year), '$'+str(secondHalf)]
                                    )
                        elif month == 2:
                            if year % 4 == 0:
                                cursor.execute("INSERT INTO payrolllist (employeeid, payperiod, amountpaid) VALUES (%s, %s, %s)",
                                            [eID[0], str(16)+'/'+str(month)+'/'+str(year)+' - '+str(29)+'/'+str(month)+'/'+str(year), '$'+str(secondHalf)]
                                        )
                            else:
                                cursor.execute("INSERT INTO payrolllist (employeeid, payperiod, amountpaid) VALUES (%s, %s, %s)",
                                            [eID[0], str(16)+'/'+str(month)+'/'+str(year)+' - '+str(28)+'/'+str(month)+'/'+str(year), '$'+str(secondHalf)]
                                        )
                        elif month == 4 or month == 6 or month == 9 or month == 11:
                            cursor.execute("INSERT INTO payrolllist (employeeid, payperiod, amountpaid) VALUES (%s, %s, %s)",
                                        [eID[0], str(16)+'/'+str(month)+'/'+str(year)+' - '+str(30)+'/'+str(month)+'/'+str(year), '$'+str(secondHalf)]
                                    )


        # print everything in payrollist
        cursor.execute("SELECT * FROM payrolllist")
        answer = cursor.fetchall()





    return employeeID, years, payment, answer


def checkReportID(reportID):
    with connection.cursor() as cursor:
        cursor.execute("SELECT reportid FROM reportidchecklist WHERE reportid=%s", [reportID])
        ret = cursor.fetchall()
        if not ret:
            cursor.execute("INSERT INTO reportidchecklist (reportid) VALUES (%s)",
                        [reportID]
                    )
            return True
        else:
            return False

def remove_duplicate(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
