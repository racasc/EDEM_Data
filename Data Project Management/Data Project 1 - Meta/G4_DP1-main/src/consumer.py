from json import dumps
from json import loads

from geopy.distance import geodesic
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
    'generator',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


def create_dc_match(actual_person, friend, dist):
    user_id, user_lat, user_lon = actual_person['id'], float(actual_person['position']['lat']), float(actual_person['position']['lon'])
    friend_id, friend_lat, friend_lon = friend['id'], float(friend['position']['lat']), float(friend['position']['lon'])
    dc_match = {'user_id': user_id, 'user_lat': user_lat, 'user_lon': user_lon, 'friend_id': friend_id,
                'friend_lat': friend_lat, 'friend_lon': friend_lon, 'transport':actual_person['transport'], 'dist': dist, 'time': actual_person['time']}
    return dc_match


def nearby_friends(actual_person, friend):
    pos_user = (float(actual_person['position']['lat']), float(actual_person['position']['lon']))
    pos_friend = (float(friend['position']['lat']), float(friend['position']['lon']))
    dist = geodesic(pos_user, pos_friend).meters
    trans_user, trans_friend = actual_person['transport'], friend['transport']
    if dist <= 500 and trans_user == trans_friend:  # Send data
        print('MATCH. FRIENDS ARE NEARBY: ', dist, 'METERS')
        dc_match = create_dc_match(actual_person, friend, dist)
        # print('ENVIO MENSAJE; ', dc_match)
        producer.send('matches', value=dc_match)
        # producer.flush()
        # time.sleep(3)


def get_matches(dc):
    for actual_person in dc.values():
        friends = actual_person['friends']
        for friend in friends:
            try:
                nearby_friends(actual_person, dc[friend])
            except KeyError as e:
                # print('KEY ERROR: ',e)
                continue


while True:
    for event in consumer:
        event_data = original_data = event.value
        print('DATA RECIVED: ', event_data)
        get_matches(event_data)
