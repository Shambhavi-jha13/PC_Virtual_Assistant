import os
import pyttsx3
pyttsx3.speak("Give me Command")
print("Write here : ", end=' ')
value=input()

if(("run" in value or "execute" in value or "open" in value) and
   ("notepad" in value)):
    os.system("notepad")

elif("chrome" in value):
    os.system("chrome Google.in")
    
elif("msedge" in value or "Internet Explorer" in value or "microsoft edge" in value):
    os.system("msedge")

elif(("run" in value or "open" in value) and ("word" in value or "msword" in value
     or "microsoft word" in value)):
    os.system("winword")

elif(("run" in value or "open" in value) and ("excel" in value or "msexcel" in value
      or "MSEXCEL" in value or "Excel" in value)):
    os.system("Excel")

elif(("run" in value or "open" in value) and ("powerpoint" in value or "MSPowerpoint"
    in value or "powerpnt" in value)):
    os.system("Powerpnt")

else:
    print("Invalid Input")
