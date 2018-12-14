
import webbrowser, time, datetime, requests, bs4

print('What expiration date to you want, make sure to pick a Friday (MM/DD/YYYY)? ' )
#check if it is a friday 
in_date = input()

def date_check(in_date):
    #set up for an if statement
    in_date = datetime.datetime.strptime(in_date, '%m/%d/%Y')
    #checks if it is a friday
    n = in_date.weekday()
    #converts the input to unix time if it is a friday, otherwise will throw an error
    if n == 4:
        in_date_2 = str(in_date)
        #convert to unix
        in_date_3 = time.mktime(datetime.datetime.strptime(in_date_2, "%Y-%m-%d %H:%M:%S").timetuple())
        in_date_3 = in_date_3 - 21600 #used to be 18000
        in_date_3 = int(in_date_3)
        
    else:
        print('Make sure you pick a friday')
    return in_date_3
    
date_check()