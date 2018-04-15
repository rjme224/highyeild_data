#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:49:37 2018

@author: jasonmerrick
"""

import csv

with open('sensor_sites.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('sensor_dic.csv', mode='w') as outfile:
        mydict = {rows[1]:[rows[0], rows[3],rows[2][37:49]] for rows in reader}