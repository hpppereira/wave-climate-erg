"""
Processamento dos dados de windwave dos satelites do globwave
- utiliza dados merged
"""


import os
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xray

plt.close('all')

# read globwave
# pathname = os.environ['HOME'] + '/GoogleDrive/ERG/data/globwave/proc/'
pathname_ecmwf = os.environ['HOME'] + '/GoogleDrive/ERG/data/ecmwf/'

# filename = 'globwave_windwave_ALT_ERS1_GDR.csv'
filename = 'globwave_windwave_GW_L2P_ALT_ENVI_GDR.csv'

df = pd.read_csv(filename, index_col='date', parse_dates=True)

# read ecmwf
ecmwf = xray.open_dataset(pathname_ecmwf + 'ERA_Interim_ERG.nc')

################################################
#acha o ponto mais proximo

#coordenada do ponto da boia
# lat = -22.148731
# lon = -40.146825

# elevacao do rio grande - ponto central
lon = -32.714
lat = -31.103

#coloca a mesma referencia do ECMWF (longitude de 0-360)
if lon < 0:
    ec = ecmwf.sel(longitude=lon + 360, latitude=lat, method='nearest')
else:
    ec = ecmwf.sel(longitude=lon, latitude=lat, method='nearest')


##############################################3
# df['swh'] = df.swh_calibrated


plt.figure()
plt.subplot(211)
plt.plot(df.index, df.wind_speed_alt)
plt.subplot(212)
plt.plot(df.index, df.swh)
plt.ylim(-5,5)

# plt.figure()
# plt.plot(df.index, (df.wind_speed_alt-df.wind_speed_alt.mean())/df.wind_speed_alt.std())
# plt.twinx()
# plt.plot(df.index, (df.swh-df.swh.mean())/df.swh.std(), 'r')
# plt.ylim(-5,5)

plt.figure()
plt.plot(df.index, df.wind_speed_alt)
plt.twinx()
plt.plot(df.index, df.swh, 'r')
plt.ylim(1,4)

# ---------------------------------------------------- #
# plotagem da comparacao globwave e ecmwf

plt.figure()
plt.plot(df.index, df.swh)
plt.plot(ec.time.data, ec.swh.data)
plt.xlim(df.index[0], df.index[-1])

# plt.figure()
# plt.plot(df.index, df.swh)
# plt.plot(ec.time.data, ec.swh.data)
# plt.xlim(df.index[0], df.index[-1])

plt.show()
