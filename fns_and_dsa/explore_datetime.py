from datetime import date, datetime, timedelta

current_date_time = datetime.now()

def display_current_datetime() :
    
    # return current_date_time
    print(current_date_time.strftime("%Y-%m-%d"))      
    print(current_date_time.strftime("%B %d, %Y"))     
    print(current_date_time.strftime("%H:%M:%S"))    

display_current_datetime()



number_of_days = int(input("Enter number of days :"))

def calculate_future_date() :  
    currentDate = date.today() 
    future_date = currentDate + timedelta(days=number_of_days)
    return(future_date)

print(calculate_future_date())
