# -*- coding: utf-8 -*-
"""
Created on Mon May 21 06:16:13 2018

@author: rjme2
"""

#loop through each radio used in controling irrigaiton (B?I3N(1,2,3))
def geti3csv():
    import requests
    from lxml import html
    import pandas as pd
    import io

    session_requests = requests.session()
    
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
    
        
    fullrows = [] #empty list in which all of the rows of the .csv are appended

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
                                             
        #print('finished {} {}'.format(csv_loc[i][0], csv_loc[i][1]))
