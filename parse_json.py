# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 12:53:53 2017

@author: Sayth
"""

import json

with open(r'C:\Users\Sayth\Projects\results\Randwick_2017-04-25.json', 'rb') as f:
    to_read = json.load(f)
    print(to_read["RaceDay"]["Meetings"])

    Meeting_Date = to_read["RaceDay"]["MeetingDate"]
