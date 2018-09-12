# -*- coding: utf-8
import json
#
# wanted_keys = ["RaceNumber", "RaceTime", "RaceName", "Distance", "WeatherCondition", "WeatherConditionLevel",
#                "TrackCondition", "TrackConditionLevel", "TrackRating"]
#
# deeper_keys = ["Runners", "Results"]
#
with open(r'C:\Users\Sayth\OneDrive\Projects\Folder\Results\Rosehill_2018-06-30.json', 'r') as f:
    DATA = json.load(f)
    ENTRY_POINT = DATA['RaceDay']['Meetings']
    for item in ENTRY_POINT:
        for dets in item['Races']:
            for run in  dets['RacingFormGuide']['Meeting']:
                print(run.items())
#             # for det in dets.items():  #     print(det)  #     print(det['RunnerName'])  #     if k in deeper_keys:  #  #       print(v)  #         print("{0} \t {1}".format(k, v))
#
#
print(ENTRY_POINT.keys())
#  dict_keys(['Abandoned', 'MeetingId', 'MeetingCode', 'MeetingType', 'VenueName', 'WeatherCondition',  # 'WeatherConditionLevel', 'TrackCondition', 'TrackConditionLevel', 'TrackRating', 'TrackChanged',  #  'TrackRatingChanged', 'Races', 'Pools'])
#
# ## Meeting details level.  # print("MeetingId: ", ENTRY_POINT['MeetingId'])  # print("Venue Name: ", ENTRY_POINT['VenueName'])  # print("Weather: ", ENTRY_POINT['WeatherCondition'])  # print("Track Condition: ", ENTRY_POINT['TrackCondition'])  # print("Track Rating: ", ENTRY_POINT['TrackRating'])
#
races = ENTRY_POINT['Races'][0]
#
# ## First level of feature keys  # dict_keys(['FeatureRaceBonusActive', 'FixedPriceSummary', 'RacingFormGuide', 'Status', 'RaceNumber',  # 'RaceTime', 'RaceName', 'Distance', 'WeatherChanged', 'WeatherCondition', 'WeatherConditionLevel',  # 'TrackChanged', 'TrackCondition', 'TrackConditionLevel', 'TrackRating', 'SubFavourite',  # 'SubFavouriteCandidate', 'TotalTrioAvailable', 'TotalTrioSubEventId', 'TrackRatingChanged', 'Runners',  #  'Pools', 'Tips', 'Results'])
#
# # dict_keys(['FeatureRaceBonusActive', 'FixedPriceSummary', 'RacingFormGuide', 'Status', 'RaceNumber', 'RaceTime',  #            'RaceName', 'Distance', 'WeatherChanged', 'WeatherCondition', 'WeatherConditionLevel', 'TrackChanged',  #            'TrackCondition', 'TrackConditionLevel', 'TrackRating', 'SubFavourite', 'SubFavouriteCandidate',  #            'TotalTrioAvailable', 'TotalTrioSubEventId', 'TrackRatingChanged', 'Runners', 'Pools', 'Tips',  #            'Results'])
#
# # for k, v in races.items():  #     print(k['RacingFormGuide'])  # RFG = races['RacingFormGuide'].keys()  # EVENT = races['RacingFormGuide']['Event'].keys()
#
# # print(list(RFG))  # print(list(EVENT))
#
#
def walk_json(tree, path=[]):
    try:
        for root in tree.keys():
            yield from walk_json(path + [root])
    except AttributeError:  # in case .items() is not possible (on leaves)
        yield path + [tree]
#
# # print(list(walk_json(races['RacingFormGuide']['Event']['Race']['Distance'])))