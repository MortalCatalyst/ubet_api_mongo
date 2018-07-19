import time
from datetime import timedelta, date
import requests
import pathlib
import json

# TODO: Make file downloader into a function and then convert file to module.
# TODO: Detect which OS it is on
# TODO: Download file based on appropriate OS call
# TODO: function for API's let user select which API to use then call that method (CLASS would be better)

def dateRange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


meetingCodes = ['NR', 'VR', 'QR', 'BR', 'SR', 'MR', 'VR', 'AR', 'PR', 'TR', 'ZS', 'CR', 'OS']
start_date = date(2018, 3, 20)
end_date = date(2018, 7, 22)



def dateURL(start, end):
    for sd in dateRange(start, end):
        for mc in meetingCodes:
            yield "https://api.tatts.com/sales/vmax/web/data/racing/{0}/{1}/{2}/{3}/multi/full".format(sd.strftime("%Y"),
                                                                                                 sd.strftime("%m"),
                                                                                                 sd.strftime("%d"), mc)



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
        result_path = pathlib.PurePath(r'C:\Users\Sayth\OneDrive\Projects\Folder\Results', file_name)
        pre_race_path = pathlib.PurePath(r'C:\Users\Sayth\OneDrive\Projects\pre', file_name)
        print(data["RaceDay"]["Meetings"][0]["Races"][0]["Status"])
        if status == "PAYING":
            with open(result_path, 'w') as f:
                json.dump(data, f)
        else:
            with open(pre_race_path, 'w') as f:
                json.dump(data, f)

