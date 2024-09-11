'''
Author: Yishuo Wang
Date: 2024-07-19 12:54:59
LastEditors: Yishuo Wang
LastEditTime: 2024-07-19 12:56:26
Description: get the date between start and end and return a list
'''

# generate a list of dates between StartTime and EndTime, considering leap year and the end of month
def date_range(StartTime, EndTime):
    start_year = int(str(StartTime)[0:4])
    end_year = int(str(EndTime)[0:4])
    start_month = int(str(StartTime)[4:6])
    end_month = int(str(EndTime)[4:6])
    start_day = int(str(StartTime)[6:8])
    end_day = int(str(EndTime)[6:8])
    date_list = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == start_year and month < start_month:
                continue
            if year == end_year and month > end_month:
                continue
            if month in [1, 3, 5, 7, 8, 10, 12]:
                days = 31
            elif month in [4, 6, 9, 11]:
                days = 30
            else:
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    days = 29
                else:
                    days = 28
            for day in range(1, days + 1):
                if year == start_year and month == start_month and day < start_day:
                    continue
                if year == end_year and month == end_month and day > end_day:
                    continue
                date_list.append(year * 10000 + month * 100 + day)

    return date_list
