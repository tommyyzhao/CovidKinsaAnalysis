# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:54:34 2020

@author: raymo
"""

import requests, time
import pandas as pd

#api endpoint
BASE_URL = "https://static.kinsahealth.com/"

states = "AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY".split(" ")

#initialize data frame
URL = BASE_URL + "{}_data.json".format(states[0])
r = requests.get(url = URL)
data = r.json()
kinsa_df = pd.DataFrame(data['data'], columns = data['columns'])

#appending county level data for each state
for state in states[1:]:
    print("Getting {} data".format(state))
    time.sleep(.256)
    URL = BASE_URL + "{}_data.json".format(state)
    
    r = requests.get(url = URL)
    try:
        data = r.json()
        df = pd.DataFrame(data['data'], columns = data['columns'])
        kinsa_df = kinsa_df.append(df)
    except:
        print("{} data unavailable".format(state))
        continue
    
    
kinsa_df.to_csv('kinsa_county.csv', index=False)
print("Done")