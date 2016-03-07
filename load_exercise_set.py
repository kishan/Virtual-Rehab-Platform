"""
run below command from terminal 

python load_exercise_set.py data_import/Exercise_Set.csv

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


def save_exercise_set_from_row(exercise_set_row):
    ES = Exercise_Set()
    ES.id = exercise_set_row[0]

    rehab_session_id = exercise_set_row[1]
    ES.rehab_session = Rehab_Session.objects.get(pk=rehab_session_id)

    exercise_choice = exercise_set_row[2]
    ES.exercise = exercise_choice

    sets_total = exercise_set_row[3]
    set_completed = exercise_set_row[4]
    ES.sets_total = sets_total
    ES.set_completed = sets_total

    reps_total = exercise_set_row[5]
    reps_completed = exercise_set_row[6]
    ES.reps_total = reps_total
    ES.reps_completed = reps_total

    ES.accuracy = exercise_set_row[7]
    ES.range_of_motion = exercise_set_row[8]

    ES.save()
    

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        users_df = pd.read_csv(sys.argv[1])
        print users_df

        users_df.apply(
            save_exercise_set_from_row,
            axis=1
        )

        print "There are {} exercise_sets".format(Exercise_Set.objects.count())
        
    else:
        print "Please, provide Patient file path"
