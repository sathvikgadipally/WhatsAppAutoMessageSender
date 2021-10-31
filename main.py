import pywhatkit as py


phno = input('What is the phone number?(with +91): ')
messg = input('What is the message?(leave a space at the end): ')
times = input('How many time should the message be spammed?: ')
timHrs = input('What is the time in Hours?: ')
timMin = input('What is the time in minutes?: ')
message = py.sendwhatmsg(phno, messg  * int(times), timHrs, timMin)