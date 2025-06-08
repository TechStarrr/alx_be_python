from datetime import date, datetime, timedelta

def display_current_datetime() :
    current_date_time = datetime.now()
    return current_date_time

print(display_current_datetime())



number_of_days = int(input("Enter number of days :"))

def calculate_future_date() :  
    currentDate = date.today() 
    future_date = currentDate + timedelta(days=number_of_days)
    return(future_date)

print(calculate_future_date())
