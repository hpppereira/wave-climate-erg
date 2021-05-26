"""
Concatena dados dos satelites de windwave

- as longitudes do satelite estao de 0 a 360
- as longitudes do ecmwf estao de 0 a 360
"""


import os
import numpy as np
import xarray as xray
import pandas as pd
    

sat = 'ALT_ERS1_GDR'
# sat = 'GW_L2P_ALT_ENVI_GDR'

pathname = os.environ['HOME'] + '/GoogleDrive/ERG/data/globwave/windwave/%s/' %sat

listfiles = np.sort(os.listdir(pathname))

data = []
date = []
for filename in listfiles:

    print filename

    ds = xray.open_dataset(pathname + filename)
    stop
    data.append(list([float(ds.mean()['swh'].values),float(ds.mean()['wind_speed_alt'].values)]))
    date.append(str(ds.time.values[0])[:19])

# converte para dataframe,  data como index
df = pd.DataFrame(np.array(data), index=date, columns=['swh_calibrated','wind_speed_alt'])

# index para datetime
df.index = pd.to_datetime(df.index)

# coloca nome  da coluna do index
df.index.name = 'date'

df.to_csv('globwave_windwave_%s.csv' %sat, na_rep='nan', float_format='%.2f')

