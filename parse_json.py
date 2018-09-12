# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 12:53:53 2017

@author: Sayth
"""
import json

with open(r'C:\Users\Sayth\OneDrive\Projects\Folder\Results\Rosehill_2018-06-30.json', 'r') as f:
    DATA = json.load(f)
    ENTRY_POINT = DATA['RaceDay']['Meetings'][0]
    # print(ENTRY_POINT.keys())
    # dict_keys(['Abandoned', 'MeetingId', 'MeetingCode', 'MeetingType', 'VenueName', 'WeatherCondition',
    # 'WeatherConditionLevel', 'TrackCondition', 'TrackConditionLevel', 'TrackRating', 'TrackChanged',
    #  'TrackRatingChanged', 'Races', 'Pools'])

    ## Meeting details level.
    # print("MeetingId: ", ENTRY_POINT['MeetingId'])
    # print("Venue Name: ", ENTRY_POINT['VenueName'])
    # print("Weather: ", ENTRY_POINT['WeatherCondition'])
    # print("Track Condition: ", ENTRY_POINT['TrackCondition'])
    # print("Track Rating: ", ENTRY_POINT['TrackRating'])

    races = ENTRY_POINT['Races'][0]

    ## First level of feature keys
    # dict_keys(['FeatureRaceBonusActive', 'FixedPriceSummary', 'RacingFormGuide', 'Status', 'RaceNumber',
    # 'RaceTime', 'RaceName', 'Distance', 'WeatherChanged', 'WeatherCondition', 'WeatherConditionLevel',
    # 'TrackChanged', 'TrackCondition', 'TrackConditionLevel', 'TrackRating', 'SubFavourite',
    # 'SubFavouriteCandidate', 'TotalTrioAvailable', 'TotalTrioSubEventId', 'TrackRatingChanged', 'Runners',
    #  'Pools', 'Tips', 'Results'])

    for k, v in races.items():
        print(k)

    # for k in races.items():  #     k['FixedPriceSummary'][0]['FixedPrices']