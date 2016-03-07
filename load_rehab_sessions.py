"""
run below command from terminal 

python load_rehab_sessions.py data_import/Rehab_Session.csv

"""


import sys, os 
import pandas as pd

import datetime
# from datetime import datetime
from datetime import date , time


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rehab_platform.settings")

import django
django.setup()

from dashboard.models import *


def save_rehab_session_from_row(rehab_session_row):
    RS = Rehab_Session()
    RS.id = rehab_session_row[0]

    patient_id = rehab_session_row[1]
    RS.patient = Patient.objects.get(pk=patient_id)

    doctor_id = rehab_session_row[2]
    RS.doctor = Doctor.objects.get(pk=doctor_id)

    session_date = rehab_session_row[3] #YYYY-mm-dd
    session_time = rehab_session_row[4] # h:m
    session_date_time = session_date + " " + session_time
    RS.app_date_time = datetime.datetime.strptime(session_date_time, '%Y-%m-%d %H:%M')

    RS.app_lenth = rehab_session_row[5]
    RS.status = rehab_session_row[6]

    RS.save()
    

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        users_df = pd.read_csv(sys.argv[1])
        print users_df

        users_df.apply(
            save_rehab_session_from_row,
            axis=1
        )

        print "There are {} rehab_session".format(Rehab_Session.objects.count())
        
    else:
        print "Please, provide Patient file path"
