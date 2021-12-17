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

def append_pulse(pulse_dict,
                 IQ_data,
                 timestamp_format = '%Y%m%d%H%M%S%f', timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f'), pulseID=0):
    # appends the demo pulse to the list of pulses
    pulse_dict['pulses'].append(
        {
        'pulseID': pulseID,
        'timestamp': timestamp,
        'timestamp_format': timestamp_format,
        'IQ_data': IQ_data
        })

def main():
    # Creates the dictionary to hold the pulses with some demo header data
    pulse_dict = {'name': 'Demo pulses', 'purpose': 'This is a demo pulse to show how JSON files work'}

    # Creates a timestamp for the overall data
    timestamp_format = '%Y%m%d%H%M%S'
    timestamp = datetime.now().strftime(timestamp_format)
    pulse_dict['timestamp'] = timestamp
    pulse_dict['timestamp_format'] = timestamp_format

    # Creates a list to hold the pulses inside the dictionary
    # put this first due to the LIFO way JSON is written
    pulse_dict['pulses'] = []

    # creates a variable for a pulse label
    next_pulse=12345

    for i in [1,2]:
        # reads in the data from the csv file
        csv_file = "pulse_short_"+str(i)+".csv"
        IQ_data = pd.read_csv(csv_file).to_dict(orient='list')
        append_pulse(pulse_dict,IQ_data,pulseID=i)
        # read_pulse_from_csv(pulse_dict, csv_file, i)

    # # reads in the data from the csv file
    # csv_file = "pulse_short_2.csv"
    # read_pulse_from_csv(pulse_dict, csv_file, next_pulse)
    #
    # # Increments the pulse label
    # next_pulse+=1

    # Writes the dictionary to a file
    # (Using the timestamp from above to create unique filenames. Should probably use something better in production)-OC
    with open('data'+timestamp+'.json', 'w') as outfile:
        json.dump(pulse_dict, outfile)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()



