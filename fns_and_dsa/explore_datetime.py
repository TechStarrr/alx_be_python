from datetime import date, datetime, timedelta

current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime() :
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return(current_date_time)

display_current_datetime()



number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date() :  
    currentDate = date.today() 
    future_date = currentDate + timedelta(days=number_of_days)
    return(future_date.strftime("%Y-%m-%d"))

print(calculate_future_date())