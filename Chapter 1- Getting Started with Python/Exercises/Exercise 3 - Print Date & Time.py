print("Exerise 3 - Print date & Time")
print()
import datetime
now = datetime.datetime.now()
print("The date and time in where you are right now is:")
print(now.strftime("%B - %d - %Y \n %H: %M: %S %p "))
print()
print("Locale\'s Setup")
print(now.strftime("%c")) 