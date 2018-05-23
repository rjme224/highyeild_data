# -*- coding: utf-8 -*-
"""
Created on Wed May 23 06:52:53 2018

@author: rjme2
"""
import os
import pandas as pd
fullrows = []
lstrow = []
lastrow = pd.DataFrame()

directory = r'C:/users/rjme2/onedrive - university of florida/sensor_access/csv_files/all_sensors/csvs'
os.chdir(directory)
for i in os.listdir(directory):
    df = pd.read_csv(i) 
    #change column heading to an accessable form
    df.columns = ['junk','Datetime_UTC', 'M5','M15','M25','M35','M45','M55','M65','M75',
                  'M85','T5','T15','T25','T35','T45','T55','T65','T75','T85',
                  'S5','S15','S25','S35', 'S45','S55','S65','S75','S85','radio','sensors','field']
    
                                       #add 'Field' column to the df that contains (N)orth or (S)outh     
    fullrows.append(df)                                                 #append df to the 'fullrows' list
    lastrow = df[-1:]                                                   #create a df containing the last rows (most recent reading) of .csv
    lstrow.append(lastrow)   
                                         #append the last row of df to the 'lastrow' list
    print('finished {}'.format(i))
full = pd.concat(fullrows, ignore_index=True)                           #concat each list into one df
last = pd.concat(lstrow, ignore_index=True)                             #add 'total' column that adds the columns from 1(5cm depth) to 6(45cm depth)

os.chdir(r'c:/users/rjme2/onedrive - university of florida/sensor_access/csv_files/all_sensors')
dateform = datetime.datetime.now()
#convert input depth to cm and round to nearest 10cm to be consistent with 
#raw data
fname = dateform.strftime('%m%d%y%H%m')

full.to_csv('{}_full.csv'.format(fname))
last.to_csv('{}_last.csv'.format(fname))
