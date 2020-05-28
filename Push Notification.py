#pip install win10toast

from win10toast import ToastNotifier
import time #to find the time we need time package

while True: #infinite loop
  current_time=time.strftime("%H:%M:%S)   #check the current time
  if current_time=="24:00:00";
    print(current_time)
    break  #time matches while loop will break, reach the push variable
  else:
    pass
    
push=ToastNotifier()
push.show_toast("Notification","This is the notification message")  #"title","message","icon_path","duration","threaded"
