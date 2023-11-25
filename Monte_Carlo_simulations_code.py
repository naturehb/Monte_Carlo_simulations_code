import pandas as pd
import numpy as np
from math import radians, sin, cos, asin, sqrt
import datetime

def haversine_dis(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    aa = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(aa))
    r = 6371  
    return c * r


file_name = r'1.csv'
df1 = pd.read_csv(file_name)
file_name2 = r'1000.csv'
df2 = pd.read_csv(file_name2)
df2.rename(columns = {'name':'name1'}, inplace = True)
m = pd.concat([pd.concat([df1] * len(df2)).sort_index().reset_index(drop=True),
               pd.concat([df2] * len(df1)).reset_index(drop=True)], 1)
m['dis'] = m[['lon1', 'lat1', 'lon2', 'lat2']].apply(
    lambda x: haversine_dis(x['lon1'], x['lat1'], x['lon2'], x['lat2']), axis=1)

le=1000
gb=3

def x2p(x):
    if 1 > x:
        p = 0.6694
    elif 1 < x <= 3:
        p = 0.2231
    elif 3 < x <= 10:
        p = 0.0744
    elif 10 < x <= 20:
        p = 0.0248
    elif 20 < x <= 40:
        p = 0.0083
    elif 40 < x <= 60:
        p = 0.0000
    elif 60 < x :
        p = 0.000
    return p

b=0.0196
ca=0.0608

def gain_c(m):
    c = 0
    q = m['p']
    x = m['dis']
    if 1 > x:
        c = (0.6694 / q)  * x * (b * 0.1 + ca * 0.1)

    if 1 < x <= 3:
        c = (0.2231 / q)  * x * (b * 0.2667 + ca * 0.5333)

    if 3 < x <= 10:
        c = (0.0744 / q) * x * (b * 0.25 + ca * 0.75)

    if 10 < x <= 20:
        c = (0.0248 / q)  * x * (b * 0.20 + ca * 0.80)

    if 20 < x <= 40:
        c = (0.0083 / q) * x * (b * 0.1667 + ca * 0.8333)

    if 40 < x <= 60:
        c = (0.000 / q) * x * (b * 0.1429 + ca * 0.8571)

    if x > 60:
        c = (0.000 / q)  * x * (b * 0.1250 + ca * 0.8750)

    return c
def gain_p(x, m):
    
    temp = m[m['name1']==x]
    p = []
    for i in temp['dis']:
        p.append(p(i))
    return sum(p)



m['p'] = m['name1'].apply(lambda gain_p(x,m))
m['c'] = m.apply(gain_c, axis=1)

print(m)
print(np.sum(m['dis']))

print(np.mean(m['dis']))

print(np.sum(m['c'])/le)

print(np.mean(m['c']))

print(np.sum(m['c']))

print(file_name)

# data = {[np.mean(m['dis'])], [np.sum(m['c'])/le], [ca], [b], [gb],[np.sum(m['c'])], [np.mean(m['c'])], [np.sum(m['dis'])], [file_name]}
df = pd.DataFrame(data)

res=file_name+'---'+file_name2
time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# df.to_excel( res +time+ '.xlsx', index=False)
