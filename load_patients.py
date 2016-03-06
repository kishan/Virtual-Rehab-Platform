"""
run below command from terminal 

python load_patients.py data_import/patients.csv

"""


import sys, os 
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rehab_platform.settings")

import django
django.setup()

from dashboard.models import Patient, Doctor


def save_patient_from_row(patient_row):
    patient = Patient()
    patient.id = patient_row[0]
    patient.first_name = patient_row[1]
    patient.last_name = patient_row[2]
    patient.DOB = patient_row[3]
    patient.pub_date = patient_row[4]
    patient.gender = patient_row[5]
    patient.rehab_focus = patient_row[6]
    patient.phone_number = patient_row[7]
    street = patient_row[8]
    city = patient_row[9]
    state = patient_row[10]

    patient.address = street + ", " + city + ", " + state
    patient.previous_injuries = patient_row[11]
    patient.notes = patient_row[12]
    patient.recovery_percentage = patient_row[13]
    doctor_id = patient_row[14]
    patient.doctor = Doctor.objects.get(pk=doctor_id)
    dummy_image = patient_row[15]
    patient.dummy_image = dummy_image
    last_appointment = patient_row[16]
    next_appointment = patient_row[17]

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
