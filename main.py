import pywhatkit as py


phno = input('What is the phone number?(Make sure that you enter your country''s dial code'): ')
messg = input('What is the message?(leave a space at the end): ')
times = input('How many time should the message be sent?: ')
timHrs = input('What is the time(hours)?: ')
timMin = input('What is the time(minutes)?: ')
message = py.sendwhatmsg(phno, messg  * int(times), timHrs, timMin)
