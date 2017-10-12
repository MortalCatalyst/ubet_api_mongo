import time
from datetime import timedelta, date
import requests
import pathlib
import json

# TODO: Tidy up variables and create file into a module.


def dateRange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


meetingCodes = ['SR', 'MR', 'BR', 'PR']
start_date = date(2017, 1, 1)
end_date = date(2017, 10, 12)


def dateURL(start, end):
    for sd in dateRange(start, end):
        for mc in meetingCodes:
            yield "https://api.tatts.com/sales/vmax/web/data/racing/{0}/{1}/{2}/{3}/full".format(
                sd.strftime("%Y"), sd.strftime("%m"), sd.strftime("%d"), mc)


pre_path = pathlib.Path(r'C:\Users\Sayth\Projects\pre')

fullUrl = dateURL(start_date, end_date)

for dates in fullUrl:
    # print(dates)
    time.sleep(0.3)
    r = requests.get(dates)
    data = r.json()
    if data["RaceDay"] is not None:
        a = data["RaceDay"]["MeetingDate"]
        b = a[:10]
        status = data["RaceDay"]["Meetings"][0]["Races"][0]["Status"]
        file_name = data["RaceDay"]["Meetings"][0]["VenueName"] + '_' + b + '.json'
        result_path = pathlib.PurePath(r'C:\Users\Sayth\Projects\results',
                                       file_name)
        pre_race_path = pathlib.PurePath(r'C:\Users\Sayth\Projects\pre',
                                         file_name)
        print(data["RaceDay"]["Meetings"][0]["Races"][0]["Status"])
        if status == "PAYING":
            with open(result_path, 'w') as f:
                json.dump(data, f)
        else:
            with open(pre_race_path, 'w') as f:
                json.dump(data, f)

            # print(data["RaceDay"]["Meetings"][0]["Races"][0]["Status"])
    # if data["RaceDay"] is not None:
    #     client = MongoClient('localhost', 27017)
    #     db = client.ubet_ap
    #     COLLECTION = db.ubet_api
    #
    #     RESULT = db.result
    #     RESULT_ID = RESULT.insert_one(data).inserted_id

    # if data["RaceDay"] is None:
    #     print("Nothing here")
    # else:
    #     print(data["RaceDay"])
    # if data["RaceDay"]["Success"] == 'False':
    #     print('Nothing here')
# pp = pprint.PrettyPrinter(indent=2)
# data = r.json()
# print(data)

# print(db.collection_names(include_system_collections=False))
# CURSOR = db.result.find({})

# for item in CURSOR:
#     print(item)
