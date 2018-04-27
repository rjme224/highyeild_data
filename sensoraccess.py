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
import sys
import datetime
import os

email = 'rj.merrick@ufl.edu'   #Username for Highyieldag.com website
password = 'P^thon32'        #Password for Highyeildag.com
directory = input('Where do you want to save .csv files?  ')
depth = float(input("What depth (in)?  "))
if depth <= 4:
    cell = 2
    depth_mm = 100
elif depth >=4 and depth <8:
    cell = 3
    depth_mm = 200
elif depth >8 and depth <=12:
    cell = 4
    depth_mm = 300
elif depth >12 and depth <=16:
    cell = 5
    depth_mm = 400
elif depth >16 and depth <=20:
    cell = 6
    depth_mm = 500
elif depth >20 and depth <=24:
    cell = 7
    depth_mm = 600
elif depth >24 and depth <=28:
    cell = 8
    depth_mm = 700
elif depth >28 and depth <=36:
    cell = 9
    depth_mm = 800
else:
    print("depth is out of range.")
    sys.exit()

        

#dictionary containing the field id, field (North or South), and information
#regarding the web address of each .csv file. csv_loc[i][2] is the last split
#of the web address and is used when looping through the web addresses. 
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


#i3 is a list of radios associated with the B?I3N? plots from which sensor 
#based irrigation scheduling is derived
i3 = ['ASR-8103', 'ASR-8108', 'ASR-8111', 'ASR-8112', 'ASR-8117', 'ASR-8120', 
      'ASR-8125', 'ASR-8129', 'ASR-8130', 'ASR-8137', 'ASR-8147', 'ASR-8154',
      'ASR-8156', 'ASR-8157', 'ASR-8158', 'ASR-8161', 'ASR-8115', 'ASR-8106',
      'ASR-8152', 'ASR-8155', 'ASR-8159', 'ASR-8168']


LOGIN_URL = "https://myfarm.highyieldag.com/login" 

session_requests = requests.session() #opoen a persistent session to the login

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
lstrow = []  #empty list that in which the last row of the .csv is appended
fullrows = [] #empty list in which all of the rows of the .csv are appended
full = pd.DataFrame() #empty dataframe that will contain a concatination of 'fullrows'
last = pd.DataFrame() #empty dataframe that will contain a concat..of 'lstrow'

#loop through each radio used in controling irrigaiton (B?I3N(1,2,3))
for i in i3:
    URL = "http://myfarm.highyieldag.com/getcsv/{}/0".format(csv_loc[i][2]) 
    result = session_requests.get(URL, headers=dict(referer=URL))       #produce a request object of the required .csv file
    df = pd.read_csv(io.StringIO(result.text)) 
    #change column heading to an accessable form
    df.columns = ['Datetime_UTC', 'M5','M15','M25','M35','M45','M55','M65','M75',
                  'M85','T5','T15','T25','T35','T45','T55','T65','T75','T85',
                  'S5','S15','S25','S35', 'S45','S55','S65','S75','S85']
    
    df['Radio'] = i                                                     #produce a pd.DataFrame object
    df['Sensor'] = csv_loc[i][0]                                        #add 'Sensor'column to the df that contains the plot_id
    df['Field'] = csv_loc[i][1]                                         #add 'Field' column to the df that contains (N)orth or (S)outh     
    fullrows.append(df)                                                 #append df to the 'fullrows' list
    lastrow = df[-1:]                                                   #create a df containing the last rows (most recent reading) of .csv
    lstrow.append(lastrow)                                              #append the last row of df to the 'lastrow' list
    print('finished {} {}'.format(csv_loc[i][0], csv_loc[i][1]))
full = pd.concat(fullrows, ignore_index=True)                           #concat each list into one df
last = pd.concat(lstrow, ignore_index=True)                             #add 'total' column that adds the columns from 1(5cm depth) to 6(45cm depth)
last['total'] = last.iloc[:, 1:cell].sum(axis=1)                        #convert to percent and add 'pct' column to df   
last['pct'] = (last['total']/depth_mm)*100                              #find the row associated with the minimum moisture value


#use system datetime and the depth from input to create a unique filename
dateform = datetime.datetime.now()
#convert input depth to cm and round to nearest 10cm to be consistent with 
#raw data
depthcm = str(int(round((depth*2.54),-1)))
fname = dateform.strftime('%m%d%y%H%m_'+depthcm+'cm.csv')

#save the data to selected directory
os.chdir(directory)                  
last.to_csv(fname)
                                                                         

def findmin(field_name):
    '''Find the minimum sensor value.'''
    sub = last.loc[last['Field'] == field_name] 
    minrow = sub.loc[sub['pct'] == sub['pct'].min()]                        
    min_moisture = float(round(minrow['pct'], 2))                            #set the minimum moisture percent rounde to 2 places
    low_sensor = str(minrow['Sensor'])                                        #Sensor associated with the minimum moisture value
    low_field = str(minrow['Field'])                                          #Field associated with the minimum moisture value    
    low_datestamp = str(minrow.Datetime_UTC)                            #Date/time minimum moisture was recoreded
    L_sens = low_sensor[5:12]
    L_field = low_field[5:7]                                                  #convert "LOW" returns into strings useful for printing        
    L_date = low_datestamp[5:24]
    df = sub[['Datetime_UTC', 'Sensor', 'Field', 'pct']]
    df = df.sort_values('pct')
    print(df)
    print('')
    print('')
    print("The lowest moisture content is {}% from {} in the {} field at {} UTC.".format(min_moisture,
                                                                               L_sens,
                                                                               L_field,
                                                                               L_date))
north = findmin('N')
south = findmin('S')
session_requests.close()                                                #Close the session
#f = north[['Timestamp (UTC)','Sensor','Field','pct']] 
#final = f.sort_values('pct')                                            #create a printable df with desired information
#print(final)
#print('')
#print('')
#print("The lowest moisture content is {}% from {} in the {} field at {} UTC.".format(min_moisture,
#                                                                               L_sens,
#                                                                               L_field,
