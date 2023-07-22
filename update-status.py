#!/usr/bin/env python
import os
from csv import DictReader
from datetime import datetime
from zoneinfo import ZoneInfo
from jinja2 import Environment, FileSystemLoader
from itertools import groupby

__version__ = '1.0'

status_file = "status.csv"
maintenance_file = "maintenance.csv"
now = datetime.now(tz=ZoneInfo("Europe/London"))


def status_key_func(k):
    return k['servicegroup']


def man_key_func(k):
    return k['state']


def get_csv_file_data(file_name, group_by_key):
    group_by = dict()
    with open(file_name) as file_obj:
        dict_reader = DictReader(file_obj)
        list_of_dict = list(dict_reader)

    list_of_dict = sorted(list_of_dict, key=group_by_key)

    for key, value in groupby(list_of_dict, group_by_key):
        group_by.update({key: list(value)})

    return group_by


if __name__ == '__main__':
    # Get the current date and time, so we have it for use within the script.
    update_date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    print("Updating index.html...", end=" ")
    status_file_dict = get_csv_file_data(status_file, status_key_func)
    man_file_dict = get_csv_file_data(maintenance_file, man_key_func)

    state_list = list()
    for i in man_file_dict:
        state_list.append(i)

    state_list = [i for i in state_list if i]

    jinjaenv = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'www/templates')))
    index_template = jinjaenv.get_template('index-template.html')
    data = {
        'update_date': update_date_time,
        'title': "My Status Page, Upcoming Maintenance and Updates",
        'status_title': "Service Status",
        'man_title': "Upcoming Maintenance and Updates",
        'status_data': status_file_dict,
        'man_data': man_file_dict,
        'state_list': state_list,
    }
    index_file = index_template.render(data)
    with open('www/index.html', 'w') as f:
        f.write(index_file)
    print("[DONE]")
