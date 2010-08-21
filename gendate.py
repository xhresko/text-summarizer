#!/usr/bin/python3

from datetime import date,timedelta

#100819_000022

today = date.today()

yesterday = today - timedelta(1)

today = yesterday

print(today)

year = str(today.year-2000).zfill(2)
month = str(today.month).zfill(2)
day = str(today.day).zfill(2)

for i in range(120):
    anum = str(i).zfill(6)

    lnstring = year + month + day + '_' + anum
    print (lnstring)
