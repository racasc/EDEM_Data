import pandas as pd
import pickle

dc = pickle.load(open('user_example.pickle','rb'))

mlen = 0
for e in dc.values():
    print(e)
    exit(0)