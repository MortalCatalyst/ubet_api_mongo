import time
from datetime import timedelta, date
import requests
import pymongo
from pymongo import MongoClient


def dateRange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


meetingCodes = ['SR', 'MR', 'BR', 'AR', 'PR']
start_date = date(2017, 9, 6)
end_date = date(2017, 10, 1)


def dateURL(start, end):
    for sd in dateRange(start, end):
        for mc in meetingCodes:
            yield "https://api.tatts.com/sales/vmax/web/data/racing/{0}/{1}/{2}/{3}/full".format(sd.strftime("%Y"),
                                                                                                 sd.strftime("%m"),
                                                                                                 sd.strftime("%d"), mc)


fullUrl = dateURL(start_date, end_date)

for dates in fullUrl:
    # print(dates)
    time.sleep(0.3)
    r = requests.get(dates)
    data = r.json()

    if data["RaceDay"] is not None:
        client = MongoClient('localhost', 27017)
        db = client.ubet_api
        COLLECTION = db.ubet_api

        RESULT = db.result
        RESULT_ID = RESULT.insert_one(data).inserted_id

        # if data["RaceDay"] is None:
        #     print("Nothing here")
        # else:
        #     print(data["RaceDay"])
        # if data["RaceDay"]["Success"] == 'False':
        #     print('Nothing here')
# pp = pprint.PrettyPrinter(indent=2)
# data = r.json()
# print(data)

print(db.collection_names(include_system_collections=False))
CURSOR = db.result.find({})

for item in CURSOR:
    print(item)
