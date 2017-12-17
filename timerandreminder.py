#import time and datetime modules
import time
import datetime

# define variable for choice
ch = input ("Which utility do you wish to use : \n\t1. Timer \n\t2. Reminder  \nEnter your choice : ")


# choice #1 (timer) this will ask user to enter timer time and will get notified once timer is up
if ch == '1':
    timer = int(input("Enter the time in seconds for the timer :"))
    input( "Press 'Enter' to start the timer...")
    print ("timer started!")
    time.sleep(timer)
    print ("Times up!")
# choice #2 ( reminder) this will ask user to input what do they want to be reminded of task at givent time by user(yyyy/mm/dd hh:mm:ss) 
elif ch == '2':
    reminder = input ("What do you want me to remind you of? ")
    remind = datetime.datetime.strptime(input("When do you want me to remind you? ('YYYY/MM/DD hh:mm:ss') : "), '%Y/%m/%d %H:%M:%S')
    currtime = datetime.datetime.now()
    time.sleep((remind-currtime).total_seconds())
    print ("Hey! Its " + remind.strftime('%Y/%m/%d %H:%M:%S') + "\nHere's your reminder :")
    print (reminder)

else:
    print("Invalid Choice!!")
