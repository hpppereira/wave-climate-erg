"""
Merge dos dados de altimetria do GlobWave

Altimetro

- Cria lista com links dos dados para baixar os arquivos
- Baixa os dados em nc.gz (zipados)
- Descompacta os dados gerando os nc
- Carrega os nc e cria nc unico com o merge dos dados

Central lon: -32.714 lat: -31.103

1 -39.706 -26.794
2 -28.665 -26.738
3 -39.734 -36.936
4 -28.693 -36.908

getgranulelist.py --product=GW_L2P_ALT_ERS1_GDR --date=1994-02-01T00:00:00,1994-02-02T00:00:00 --bbox=-60.,60.,-100.,0. --url

"""

# import getgranulelist

import os
import xarray as xray

pathnc = '/home/hp/GoogleDrive/ERG/data/globwave/windwave/'

# lista de satelites
sats = [
        'EUR-L2P-AVHRR_METOP_A',
        'UPA-L2P-ATS_NR_2P',
        'JPL-L2P-MODIS_A',
        'NAVO-L2P-AVHRR19_G',
        'NAVO-L2P-AVHRR19_L',
        'QSCATL2B',
        'OSI_SAF-ASCAT-METOP_A',
        'GW_L2P_SAR_ENVI_GDR',
        'GW_L2P_ALT_JAS1_GDR',
        'GW_L2P_ALT_JAS2_GDR',
        'GW_L2P_ALT_ERS2_GDR',
        'GW_L2P_ALT_ERS1_GDR',
        'GW_L2P_ALT_ENVI_GDR',
        'GW_L2P_ALT_TOPX_GDR',
        'GW_L2P_ALT_GFO_GDR',
        'GW_L2P_ALT_GEOS_GDR'
        ]

datei = '2002-06-01T00:00:00'
datef = '2010-06-20T00:00:00'

loni = -39.734
lonf = -28.665
lati = -36.936
latf = -26.738

# pathname = os.environ['HOME'] + '/GoogleDrive/ERG/data/GlobWave/'

# listfiles = os.listdir(pathname)
# filename = 'GW_L2P_ALT_ERS1_GDR_19940201_000000_19940201_004551_115_0061.nc'
# # filename = listfiles[0]

# # leitura dos dados em nc
# ds = xray.open_dataset(pathname + filename)

# 

for s in sats[12:13]:

    print s

    string = '--product=%s --date=%s,%s --bbox=%s,%s,%s,%s --url' %(s,datei, datef, loni, lati, lonf, latf) 

    print 'Baixando arquivo: %s \n' %string

    os.system('python getgranulelist.py %s' %string)

    print ('-----------------')


# string = 'python getgranulelist.py --product=%s --date=%s,%s --bbox=%s' %(sats[10], datei, datef,  ) 

# os.system('python getgranulelist.py --product=GW_L2P_ALT_ERS1_GDR --date=1994-02-01T00:00:00,1994-03-02T00:00:00 --bbox=-39.734,-28.665,-36.936,-26.738 --url')
