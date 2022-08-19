import requests, json, time, datetime, os, platform
from time import sleep
from datetime import datetime, timedelta

# Execution time config
totalRunTime = 600 #mins
gapBetweenRuns = 60 #seconds

# Login details 
url = "https://jd7n1axqh0.execute-api.ca-central-1.amazonaws.com/api/reservation?facility=Joffre%20Lakes&park=Joffre%20Lakes%20Provincial%20Park"
apptDate = "2022-08-21"

# Alert tone details 
alertMP3Location="alert.mp3"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getAvailableAppointments():
    respStr = requests.get(url)
    resp = respStr.json()
    if respStr.status_code == 200:
        print(bcolors.OKGREEN + resp[apptDate]['DAY']['capacity']+ bcolors.ENDC)
        if resp[apptDate]['DAY']['capacity'] != 'Full':
            print(bcolors.FAIL + "***AVAILABLE***" + bcolors.ENDC)
            os.system('say "Appointment available. Book pass for Joffre lake."')
        return None
    return resp

#Loop through all posIDs for 2 mintues with 10 seconds gap between each request
timeout = time.time() + totalRunTime * 60   # Run for these many seconds
while True:
    if time.time() < timeout:
        print('------------START : Checking for appointment at ' + time.ctime() + '---------')
        getAvailableAppointments()
        print('------------END : Checking for appointment at ' + time.ctime() + '---------')                
        sleep(gapBetweenRuns) # Wait for these many seconds before checking again
    else:
        break #Exit once the timeout completes
