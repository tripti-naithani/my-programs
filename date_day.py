leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
non_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
month_name = ["jan" , "feb" , "mar" , "apr" , "may" ,"jun" ,"jul" , "aug" , "sep" , "oct" , "nov" ,"dec"]

def year_extractor(input_date) :
    year = input_date[-4:]
    return year

def month_extractor(input_date) :
    month=""
    for i in input_date :
        if (i == " " or i=="," or i==" ,") :
            month = input_date[input_date.index(i) + 1 : input_date.index(i) + 4]
    return month.lower()

def date_extractor(input_date) :
    day=""
    for i in input_date :
        if (i != " " or i==" ," or i==",") :
            day += i
        else :
            break
    return day

def is_leap_year(year) :
    if (year % 4 == 0) :
        if (year % 100 ==0) :
            if (year % 400 == 0) :
                return True
            else :
                return False
        else :
            return True
    return False

def day_number(month, day, year) :
    total_days = int(day)
    month_index = month_name.index(month)
    if (is_leap_year(int(year))) :
        total_days += sum(leap_year[:month_index])
    else :
        total_days += sum(non_leap_year[:month_index])

    return total_days

def date_convertor(input_date) :
    year = year_extractor(input_date)
    month = month_extractor(input_date)
    day = date_extractor(input_date)
    return  year + str(day_number(month,day,year))



input_date= input()
print(date_convertor(input_date))
