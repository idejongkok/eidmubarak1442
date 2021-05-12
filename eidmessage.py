import time
import os

messageBeforeEid = "Ramadhan will leave us soon.\nHope we can meet Ramadhan for the next year."

today = time.strftime("%d/%m/%Y")

eidTime= "13/05/2021"

user= os.popen('whoami').read()

eidMessage = ("Happy Eid :) " + '%s' %user  + "Please forgive for all my mistakes")

if today < eidTime:
    print (messageBeforeEid)
elif today == eidTime:
    print (eidMessage)
elif today > eidTime:
    print ('Today is ' '%s' 'Do not miss to fast 6 days in Shawal' %today)
else:
    quit()

