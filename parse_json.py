# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 12:53:53 2017

@author: Sayth
"""
import dpath.util
import collections
from collections import OrderedDict
import json
from pprint import pprint

with open(r'/home/sayth/Projects/results/Canterbury_2017-01-20.json', 'rb') as f, open('socks3.json','w') as outfile:
    to_read = json.load(f)


    print(to_read.keys())
    # pprint(to_read)
    meet = to_read["RaceDay"]["Meetings"]
    meeting_id = to_read["RaceDay"]["Meetings"][0]
    pprint(meeting_id.keys())
    # result = meeting_id["Races"][1]["RacingFormGuide"]["Event"]["Runners"]
    result = meeting_id["Races"]
    # for item in result:
    #     pprint(["RacingFormGuide"]["Event"]["Runners"])

    runner_lists = {}
    for n, item in enumerate(result):
        # if this one is interested / not -filtered:
        print(n, item)
        runner_lists[n] = result[n]["RacingFormGuide"]["Event"]["Runners"]

    print(runner_lists)

    # # Meeting_Details = to_read["RaceDay"]["Meetings"][0]["Races"][0]["FixedPriceSummary"]["FixedPrices"]
    # # print(Meeting_Date)
    # # result = dpath.util.search(to_read, "RaceDay/Meetings/0/Races/0/RacingFormGuide/Event/Race")
    # # result = dpath.util.get(to_read, "RaceDay/Meetings/0/Races/0/FixedPriceSummary/FixedPrices/0/MeetingId")
    # result = to_read['RaceDay']['Meetings'][0]['Races'][1]['RacingFormGuide']['Event']['Runners']
    # # output = collections.ChainMap(meet, result)
    # # json.dump(result, outfile, indent=4, sort_keys=True)
    # # output = {**meet, **result}
    output = runner_lists
    json.dump(output, outfile, indent=4, sort_keys=True)
    # print(meeting_id)