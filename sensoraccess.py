#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 09:22:38 2018

@author: jasonmerrick
"""

import requests
from lxml import html
import pandas as pd
import io

email = 'rj.merrick@ufl.edu'
password = 'P^thon32'
csv_loc = {'ASR-8103': ['B3I3N2', 'N', 'fvyKVh3jnUJe'],
           'ASR-8106': ['B2I3N5', 'N', 'K6eOtEurV4h8'],
           'ASR-8107': ['B2I2N2', 'S', 'Q7vuSRFe-amk'],
           'ASR-8108': ['B3I3N1', 'N', 'LsAOq2FuwBhx'],
           'ASR-8110': ['B4I1N2', 'N', 'Jl8RyZnD-cUB'],
           'ASR-8111': ['B4I3N3', 'N', 'bwqViopZ8Gug'],
           'ASR-8112': ['B2I3N2', 'N', 'bA94ua0rePVY'],
           'ASR-8113': ['B2I1N1', 'N', 'HphickbrtNE7'],
           'ASR-8114': ['B2I1N2', 'N', 'S6gsPe1DLqhW'],
           'ASR-8115': ['B4I3N2', 'N', 'Z4f3GuIO8zYB'],
           'ASR-8117': ['B3I3N3', 'N', 'CA60dsl3_Zxo'],
           'ASR-8118': ['B3I2N2', 'N', 'oN9WZfRtSEUd'],
           'ASR-8119': ['B2I1N3', 'N', '7ceu4sxFIVDQ'],
           'ASR-8120': ['B4I3N3', 'S', 'IRkz3lsSjX-2'],
           'ASR-8124': ['B3I5N2', 'S', 'cU0ugfkx1hHW'],
           'ASR-8125': ['B2I3N2', 'S', '_yUmMGZdjA8K'],
           'ASR-8127': ['B3I1N2', 'N', 'JVbQKWFqCaUk'],
           'ASR-8129': ['B3I3N2', 'S', 'olJcypF-Gau0'],
           'ASR-8130': ['B3I3N3', 'S', 'BDhzcTkgOjf0'],
           'ASR-8133': ['B4I2N2', 'S', 'F0xfBySpksl7'],
           'ASR-8134': ['B4I1N2', 'S', 'sNx4D1bJ9Hgk'],
           'ASR-8135': ['B4I1N3', 'N', '_sRzSM19JIBx'],
           'ASR-8137': ['B4I3N1', 'N', 'VjN-lmt8FKU0'],
           'ASR-8138': ['B3I1N3', 'N', 'MVrAcKvqpQOH'],
           'ASR-8140': ['B2I5N2', 'N', 'a8NmZoM7wD3Y'],
           'ASR-8141': ['B2I1N1', 'S', 'SwcxnpT0y_J4'],
           'ASR-8144': ['B3I1N1', 'N', 'Jegpmo8C9kZ7'],
           'ASR-8146': ['B2I5N2', 'S', 'UVJySDuspTWG'],
           'ASR-8147': ['B2I3N1', 'N', 'sYncA47V1eMm'],
           'ASR-8148': ['B4I5N2', 'N', '-PA4iv0e3V59'],
           'ASR-8149': ['B4I1N3', 'S', 'eGpFTdmjtC2H'],
           'ASR-8151': ['B2I2N2', 'N', 'CluYOvWKqSx3'],
           'ASR-8152': ['B4I3N5', 'S', 'hqkeOKUoRVmF'],
           'ASR-8153': ['B4I1N1', 'N', 'nZ1mBezUkcOg'],
           'ASR-8154': ['B2I3N1', 'S', 'XmxaOG3cpDtJ'],
           'ASR-8155': ['B3I3N5', 'S', 'NAgK3okRS0VG'],
           'ASR-8156': ['B2I3N3', 'S', 'N0vnB-sG2ect'],
           'ASR-8157': ['B4I3N1', 'S', '_zhxUYe3-g1D'],
           'ASR-8158': ['B2I3N3', 'N', 'SqXE6O4_9CMR'],
           'ASR-8159': ['B3I3N5', 'N', 'e81S2C5QKvhk'],
           'ASR-8161': ['B4I3N2', 'S', 'MWzSO5HJrxje'],
           'ASR-8163': ['B2I1N3', 'S', 'lRiJmq02y9rz'],
           'ASR-8164': ['B3I2N2', 'S', 'hbgAnjCeW7_N'],
           'ASR-8165': ['B3I5N2', 'N', 'TKa-WvVlsC_o'],
           'ASR-8166': ['B4I5N2', 'S', 'hZemyEapcbXw'],
           'ASR-8167': ['B4I1N1', 'S', 'wAOrv39elzoK'],
           'ASR-8168': ['B2I3N5', 'S', 'R8z6oHuQt3pe'],
           'ASR-8171': ['B2I1N2', 'S', '8q5pAVbIFQXJ'],
           'ASR-8173': ['B3I1N1', 'S', 'k4DAR7X8Q9eH'],
           'ASR-8174': ['B3I1N2', 'S', 'Fmne2yMl7zqk'],
           'ASR-8298': ['B4I2N2', 'N', 'beGwxJaj_oFS'],
           'ASR-8301': ['B3I1N3', 'S', '12iz9I7cQLuP']}
i3 = ['ASR-8103', 'ASR-8108','ASR-8111','ASR-8112', 'ASR-8117', 'ASR-8120', 
           'ASR-8125', 'ASR-8129', 'ASR-8130', 'ASR-8137', 'ASR-8147', 
           'ASR-8154', 'ASR-8156', 'ASR-8157', 'ASR-8158', 
           'ASR-8161', 'ASR-8115']


LOGIN_URL = "https://myfarm.highyieldag.com/login"

session_requests = requests.session()

# Get login csrf token
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath
                              ("//input[@name='csrf_token']/@value")))[0]
# Create payload
payload = {
        "email": email,
        "password": password,
        "csrf_token": authenticity_token
        }

# Perform login
result = session_requests.post(LOGIN_URL, data=payload,
                               headers=dict(referer=LOGIN_URL))


# Scrape url
lstrow = []
fullrows = []
full = pd.DataFrame()
last = pd.DataFrame()
for i in i3:
    URL = "http://myfarm.highyieldag.com/getcsv/{}/0".format(csv_loc[i][2])
    result = session_requests.get(URL, headers=dict(referer=URL))
    df = pd.read_csv(io.StringIO(result.text))
    df['Sensor'] = csv_loc[i][0]
    df['Field'] = csv_loc[i][1]
    fullrows.append(df)
    lastrow = df[-1:]
    lstrow.append(lastrow)
full = pd.concat(fullrows, ignore_index=True)
last = pd.concat(lstrow, ignore_index=True)
last['total'] = last.iloc[:, 1:6].sum(axis=1)
last['pct'] = (last['total']/550)*100

min_ = last.loc[last['pct'] == last['pct'].min()]

min_moisture = float(round(min_['pct'], 2))
low_sensor = str(min_['Sensor'])
low_field = str(min_['Field'])
low_datestamp = str(min_['Timestamp (UTC)'])
L_sens = low_sensor[5:12]
L_field = low_field[7]
L_date = low_datestamp[5:24]

session_requests.close()
final = last[['Timestamp (UTC)','Sensor','Field','pct']]
print(final)
print("The lowest moisture content is {}% from {} in the {} field at {} UTC.".format(min_moisture,
                                                                               L_sens,
                                                                               L_field,
                                                                               L_date))
