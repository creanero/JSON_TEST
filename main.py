# coding=utf-8
# JSON Pulse Writer Test
# (c) Oisin Creaner, DIAS, 9th December, 2021

import json
from datetime import datetime
import pandas as pd

def read_pulse_from_csv(pulse_data, csv_file, pulseID):
    # reads in pulse data from a file
    IQ_data = pd.read_csv(csv_file).to_dict(orient='list')
    # creates a timestamp for the pulse
    # (this should probably not be done at write time, but is here for demo purposes - OC)
    timestamp_format = '%Y%m%d%H%M%S%f'
    timestamp = datetime.now().strftime(timestamp_format)

    # appends the demo pulse to the list of pulses
    pulse_data['pulses'].append(
        {
        'pulseID': pulseID,
        'timestamp': timestamp,
        'timestamp_format': timestamp_format,
        'IQ_data': IQ_data
        })

def main():
    # Creates the dictionary to hold the pulses
    pulse_data = {}

    # Creates a list to hold the pulses inside the dictionary
    # put this first due to the LIFO way JSON is written
    pulse_data['pulses'] = []

    # Creates a timestamp for the overall data
    timestamp_format = '%Y%m%d%H%M%S'
    timestamp = datetime.now().strftime(timestamp_format)
    pulse_data['timestamp'] = timestamp
    pulse_data['timestamp_format'] = timestamp_format

    # Creates header data
    pulse_data['purpose'] = 'This is a demo pulse to show how JSON files work'
    pulse_data['name'] = 'Demo pulses'

    # creates a variable for a pulse label
    next_pulse=12345

    for i in [1,2]:
        # reads in the data from the csv file
        csv_file = "pulse_short_"+str(i)+".csv"
        read_pulse_from_csv(pulse_data, csv_file, i)

    # # reads in the data from the csv file
    # csv_file = "pulse_short_2.csv"
    # read_pulse_from_csv(pulse_data, csv_file, next_pulse)
    #
    # # Increments the pulse label
    # next_pulse+=1

    # Writes the dictionary to a file
    # (Using the timestamp from above to create unique filenames. Should probably use something better in production)-OC
    with open('data'+timestamp+'.json', 'w') as outfile:
        json.dump(pulse_data, outfile)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()



