# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import xray
import pandas as pd
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

plt.close('all')


#DATADIR = '/Users/Phellipe/Studies/Masters/Project/Thesis/Data'
#FIGDIR  = '/Users/Phellipe/Studies/Masters/Project/Thesis/Text/Chapters/Chapter_3/fig_method/'

DATADIR = os.environ['HOME'] + '/GoogleDrive/ERG/data/etopo/'

#### Bathymetry ########################################################################
########################################################################################

#### Rio de Janeiro Shelf - Nautical Charts
#grd = DATADIR + 'rio_grd.nc'
#grd = xray.open_dataset(grd)
#Gtopo = grd['hraw'].values
#Glon = grd['lon_rho'].values
#Glat = grd['lat_rho'].values

# loni = -39.734
# lonf = -28.665
# lati = -36.936
# latf = -26.738

#### SE Shelf - Etopo1
#Alims = [-48.95, -38.54, -25.14, -18.15]
Alims = [-55., -25., -40., -15.]
#Alims = [-180.0, 180.0, -60.0, 60.0 ]
#Alims = [0.0, 360.0, -60.0, 60.0 ]
etopo = DATADIR + 'ETOPO-REMO.nc'
etopo = xray.open_dataset(etopo).sel( lon=slice(Alims[0],Alims[1] ), lat=slice(Alims[2],Alims[3]) )
Etopo = etopo.z.values
Elon, Elat = np.meshgrid( etopo.lon, etopo.lat )


########################################################################################
# leitura do arquivo .nc to track do satelite

sat = 'ALT_ERS1_GDR'
# sat = 'GW_L2P_ALT_ENVI_GDR'

pathname = os.environ['HOME'] + '/GoogleDrive/ERG/data/globwave/windwave/%s/' %sat

listfiles = np.sort(os.listdir(pathname))

data = []
date = []
lat = []
lon = []


for filename in listfiles[:50]:

    print filename

    ds = xray.open_dataset(pathname + filename)

    pos = ds['swh'].loc[(ds.lat>-40) & (ds.lat<-30) & (ds.lon>-45+360) & (ds.lon<-35+360)]

    # stop



sx, sy = [-47.4,-28.5]


Lims = Alims

#Lims = [-45., -41.7, -23.70, -21.4 ]
#Lims = [-50.0, -30.0, -50.0, -15.0 ]
#Lims = [290.0, 340.0, -55.0, -15.0 ]
#Lims = [-180.0, -30.0, -33.0, -22.0 ]

m2 = Basemap(projection='cyl', resolution='l', llcrnrlon=Lims[0],\
                        llcrnrlat=Lims[2], urcrnrlon=Lims[1], urcrnrlat=Lims[3])

axmin, axmax = Lims[0], Lims[1]
aymin, aymax = Lims[2], Lims[3]

axs = [axmin,axmax,axmax,axmin,axmin]
ays = [aymin,aymin,aymax,aymax,aymin]

print 'gerou mapa base'

#########################################################################################

fig = plt.figure(figsize=(9,6), facecolor='w')

# Rio de Janeiro Shelf Area (Larger Map) #############################################################

ax1 = fig.add_subplot(111)


m2.drawcoastlines(linewidth=1)
print 'fazendo linha de costa'

# m2.drawstates(linewidth=1, zorder=12)
cs = m2.contour( Elon, Elat, Etopo*-1, [50, 100, 200, 500, 1500, 2500, 3500, 4000], colors='lightgray', linewidth=.7, alpha=0.8 )
#cs = m2.contour( Elon, Elat, Etopo*-1, [500, 2000], colors='lightgray', linewidth=.7, alpha=0.8 )
# cs.clabel(fmt='%i', fontsize=12)


m2.plot(pos.lon.data-360, pos.lat.data, '.', markerfacecolor='dodgerblue', markeredgecolor='k', mew=2, markersize=12)




fig.savefig('map_track.png', dpi=200 )


plt.show()



