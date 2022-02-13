#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import csv
import os
from pathlib import Path
import errno


# Convert milliseconds timestamp into a readable date.
def timeStampToDate(milliseconds):
    date = datetime.datetime.fromtimestamp(milliseconds / 1000.0)
    date = date.strftime('%Y-%m-%d')
    return date


# # Check time convention.
# def timeStampToAMPM(milliseconds):
#     date = datetime.datetime.fromtimestamp(milliseconds / 1000.0)
#     if date.hour < 12:
#         time_convention = "AM"
#     else:
#         time_convention = "PM"
#     return time_convention


# Returns a list of all the waypoints of a activity
a = dict()
# Set start point of activity as a list.
def activitySegment(activitySegment_dict):
    trip_id = activitySegment_dict["duration"]["startTimestampMs"]

    time_stamp = timeStampToDate(int(trip_id))
    distance = activitySegment_dict.get("distance", 0)
    try:
        ac_type = activitySegment_dict["activityType"]

    except KeyError:
        ac_type = "UNKNOWN"
    # time_convention = timeStampToAMPM(int(trip_id))
    # Formatting variables
    start_point = [time_stamp, distance, ac_type]
    if ac_type not in a:
        a[ac_type] = 1
    print(a)
    return start_point


# Method to run all the scripts.
def parse_data(data,name):
    name = name[:-5]
    parsed_data = []
    for data_unit in data["timelineObjects"]:
        if "activitySegment" in data_unit.keys():
            parsed_data.append(activitySegment(data_unit["activitySegment"]))
            print(parsed_data)

        else:
            print("Error")
    write_activity_points_csv(parsed_data,name)

def write_activity_points_csv(parsed_data,name):
    year = name[:4]
    filename = f"./parsed/{year}/{name}.csv"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(parsed_data)


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# files = ["2021_APRIL.json","2021_AUGUST.json","2021_JULY.json"]
rootdir = os.getcwd()

files = [os.path.join(root, name)
for root, dirs, files in os.walk(rootdir)
for name in files
if name.endswith(".json")]

for file in files:
    name = os.path.basename(file)
    print(file)
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    parse_data(data,name)

