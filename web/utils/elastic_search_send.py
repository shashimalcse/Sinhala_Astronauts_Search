import urllib.request as urllib2
import urllib.parse as parse
from elasticsearch import Elasticsearch,helpers
import json
import pandas as pd
import os
import csv
import math
import re

def send_data():
    es_host = os.environ['ELASTICSEARCH_URL']
    print('Elastic host is {}'.format(es_host))
    es = Elasticsearch([es_host])
    es.indices.delete(index="astronauts")
    es.indices.create(index="astronauts")
    df = pd.read_csv('./astronauts_sinhala.csv')
    pat = r'(?P<days>(\d+)(\sdays))? ?(?P<hours>(\d+)(\shours))? ?(?P<minutes>(\d+)(\sminutes))?'
    pat1 = r'(?P<d>(\d+)(d))? ?(?P<h>(\d+)(h))? ?(?P<min>(\d+)(min))?'
    pat2 = r'(?P<d>(\d+)(d))? ?(?P<h>(\d+)(h))? ?(?P<m>(\d+)(m))?'
    df = df.fillna('')
    for i in range(len(df['name'])):
        name = df['name'][i]
        bday = df['bday'][i]
        status = df['status'][i]
        nationality = df['nationality'][i]
        time_d = df['time'][i]
        time = 0
        if str(time_d)=="nan":
            continue
        result = re.match(pat1,time_d)
        time = get_time(result,time)
        if time==0:
            result = re.match(pat,time_d)
            time = get_time(result,time)
        if time==0:
            result = re.match(pat2,time_d)
            time = get_time(result,time)
        mission_names = df['mission_names'][i]
        mission_names = mission_names.strip()
        mission_names = mission_names[2:-2]
        mission_names = mission_names.split(',')
        selection = df['selection'][i]
        occupation = df['occupation'][i]
        summary = df['summary'][i]
        song_obj = {
                'Name' :name,
                'BDay' : bday,
                'Status' : status,
                'Nationality' : nationality,
                'Time' : time,
                'Mission_names' : mission_names,
                'Selection' : selection,
                'Occupation' : occupation,
                'Summary' : summary
        }
        try:
            es.index(index='astronauts', doc_type='astronaut', id=i, body=song_obj)
        except Exception as e:
                print(e)
def get_time(result,time):
    for i,k in enumerate(result.groupdict()):
        value = result.groupdict()[k]
        if value is not None:
            t = int(str(''.join(i for i in value if i.isdigit())))
            if i==0:
                time += t*60*24 
            elif i==1:   
                time +=t*60 
            elif i==2:   
                time +=t
    return time  