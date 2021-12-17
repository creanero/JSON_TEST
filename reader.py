# coding=utf-8
# JSON Pulse Writer Test
# (c) Oisin Creaner, DIAS, 9th December, 2021

import json
from datetime import datetime
import pandas as pd

def main ():
    with open('pulse_2.json.test') as json_file:
        data = json.load(json_file)
        print (data)
        for p in data['pulses']:
            pulseID = p['pulseID']
            IQ_pulse = pd.DataFrame(p['IQ_data'])
            print ('Pulse:\t'+ str(pulseID))
            print (IQ_pulse)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()