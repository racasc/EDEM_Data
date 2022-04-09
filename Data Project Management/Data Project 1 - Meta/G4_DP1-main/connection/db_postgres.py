from datetime import datetime
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine, VARCHAR, Float, TIMESTAMP, BOOLEAN, INTEGER
from sqlalchemy.pool import NullPool
pd.set_option('display.width',None)



class bbdd:

    def __init__(self):
        try:

            self.engine = create_engine("postgresql+psycopg2://{user}:{pw}@{host}/{db}".format(host='127.0.0.1',
                                                                                         db='metaverso',
                                                                                         user='root',
                                                                                         pw='metaverso'),
                                        poolclass=NullPool)

        except Exception as e:
            print('No conectado a la base de datos: ', e)

    def get_query(self, query):
        with self.engine.connect() as connection:
            print('CONNECTED')
            result = pd.read_sql(query, connection)
            connection.close()

            return result

    def set_query(self, query):
        with self.engine.connect() as connection:
            connection.execute(query)
            connection.close()

    def upload_raw_data(self, data):
        try:
            data.drop_duplicates(inplace=True)
            data = data[['id','name','last_name','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','lat','lon','transport','age','gender','weight','height','time']]
            dc_types = {'id': INTEGER(),'name': VARCHAR(length=50),'last_name':VARCHAR(length=50),'f1': INTEGER(),'f2': INTEGER(),
                        'f3': INTEGER(),'f4': INTEGER(),'f5': INTEGER(),'f6': INTEGER(),'f7': INTEGER(),'f8': INTEGER(),'f9': INTEGER(),'f10': INTEGER(),
                        'lat':Float(precision=6, asdecimal=True),'lon':Float(precision=6, asdecimal=True),'transport':VARCHAR(length=50),'age':INTEGER(),
                        'gender':VARCHAR(length=5),'weight':Float(precision=4, asdecimal=True),'height':Float(precision=4, asdecimal=True),'time':TIMESTAMP(4)
                        }
        except:
            pass
        with self.engine.connect() as connection:
            try:
                data.to_sql(name="raw_data",
                            con=connection, index=False,
                            if_exists="append", dtype=dc_types,
                            chunksize=2000, method='multi'
                            )
            except Exception as e:
                print('Error en subida: ',e)
            finally:
                connection.close()

    def upload_match(self, data):
        try:
            data.drop_duplicates(inplace=True)
            data = data[['user_id','user_lat','user_lon','friend_id','friend_lat','friend_lon','transport','distance','time']]
            dc_types = {'user_id': INTEGER(),
                        'user_lat': Float(precision=2, asdecimal=True),
                        'user_lon': Float(precision=2, asdecimal=True),
                        'friend_id': INTEGER(),
                        'friend_lat': Float(precision=2, asdecimal=True),
                        'friend_lon': Float(precision=2, asdecimal=True),
                        'transport': VARCHAR(50),
                        'distance':Float(precision=2, asdecimal=True),
                        'time':TIMESTAMP(0)}
        except:
            pass
        with self.engine.connect() as connection:
            try:
                data.to_sql(name="matches",
                            con=connection, index=False,
                            if_exists="append", dtype=dc_types,
                            chunksize=2000, method='multi'
                            )
            except Exception as e:
                print('Error en subida: ',e)
            finally:
                connection.close()
