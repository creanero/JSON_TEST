# coding=utf-8
# JSON Pulse Writer Test
# (c) Oisin Creaner, DIAS, 9th December, 2021

import json
from datetime import datetime
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Creates the dictionary to hold the pulses
    pulse_data = {}

    # Creates header data
    pulse_data['name'] = 'Demo pulses'
    pulse_data['purpose'] = 'This is a demo pulse to show how JSON files work'

    # Creates a list to hold the pulses inside the dictionary
    pulse_data['pulses'] = []

    # creates a variable for a pulse label
    next_pulse=12345

    # reads in pulse data from a file
    IQ_data = pd.read_csv('pulse_short.csv').to_json()

    # creates a timestamp for the pulse
    # (this should probably not be done at write time, but is here for demo purposes - OC)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # appends the demo pulse to the list of pulses
    pulse_data['pulses'].append(
        {
        'pulseID': next_pulse,
        'timestamp': timestamp,
        'IQ_data': IQ_data
        })

    # Increments the pulse label
    next_pulse+=1


    # Writes the dictionary to a file
    # (Using the timestamp from above to create unique filenames. Should probably use something better in production)-OC
    with open('data'+timestamp+'.txt', 'w') as outfile:
        json.dump(pulse_data, outfile)

