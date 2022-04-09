import time

from connection.db_postgres import bbdd
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from json import loads
import numpy as np

consumer_raw = KafkaConsumer(
    'generator',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=None,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

def create_friend_columns(dc):
    amigos = dc['friends']
    for c, a in enumerate(amigos):
        dc[f'f{c+1}'] = a
    for e in range(len(amigos)+1,11):
        dc[f'f{e}'] = np.nan
    return dc

def parse_columns_to_int(dc):
    columns_to_parse = ['id','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10']
    for c in columns_to_parse:
        if isinstance(dc[c], str):
            dc[c] = int(dc[c].replace('-',''))
    return dc

def transform_raw(dc_data):
    for dc in dc_data.values():
        dc['lat'], dc['lon'] = dc['position']['lat'], dc['position']['lon']
        dc = create_friend_columns(dc)
        dc = parse_columns_to_int(dc)
        [dc.pop(key,None) for key in ["position","friends"]]
        df = pd.DataFrame(dc, index=[0])
        bbdd().upload_raw_data(df)
        print('Subida ok')


while True:
    print(consumer_raw.topics())
    for event in consumer_raw:
        dc = event.value
        print(dc)
        transform_raw(dc)
