from datetime import date, timedelta

def saturday(startdate,enddate):
    dt=date(startdate,1,1)
    dt2(enddate,12,30)
    print(dt)
    print(dt2)

startdate=input('Enter StartDate:-')
enddate=input('Enter EndDate:-')
print('saturdays are:',saturday(startdate,enddate))


