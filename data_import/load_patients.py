import sys, os 
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rehab_platform.settings")

import django
django.setup()

from django.contrib.auth.models import Patient


def save_patient_from_row(user_row):
    patient = Patient()
    patient.id = patient_row[0]
    patient.first_name = patient_row[1]
    patient.last_name = patient_row[2]
    patient.DOB = patient_row[3]
    patient.pub_date = patient_row[4]
    patient.gender = patient_row[5]
    patient.rehab_focus = patient_row[6]
    patient.phone_number = patient_row[7]
    patient.address = patient_row[8]
    patient.previous_injuries = patient_row[9]
    patient.notes = patient_row[10]
    patient.recovery_percentage = patient_row[11]

    patient.save()
    

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        users_df = pd.read_csv(sys.argv[1])
        print users_df

        users_df.apply(
            save_patient_from_row,
            axis=1
        )

        print "There are {} users".format(Patient.objects.count())
        
    else:
        print "Please, provide Patient file path"