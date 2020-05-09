# Script to Download ERA5 wave spectrum using python, cdsapi module. 
# 24/09/2019 , Ricardo Campos (IST/CENTEC) riwave@gmail.com

# from ecmwfapi import ECMWFDataServer
import cdsapi
import calendar

# https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5
# https://www.ecmwf.int/en/forecasts/documentation-and-support/2d-wave-spectra

# area selected, edit line 44
# 41N 33W
# 41N 22.5W
# 36N 33W
# 36N 22.5W

c1 = cdsapi.Client()
c2 = cdsapi.Client()

# Wind and Wave Parameters
c1.retrieve('reanalysis-era5-single-levels', {
                'product_type':'reanalysis',
                'variable':['10m_u_component_of_wind','10m_v_component_of_wind','mean_wave_direction',
                            'mean_wave_period','significant_height_of_combined_wind_waves_and_swell'],
                'year':['2019'],
                'month':['01','02','03','04','05','06',
                         '07','08','09','10','11','12'],
                'day':['01','02','03',
                       '04','05','06',
                       '07','08','09',
                       '10','11','12',
                       '13','14','15',
                       '16','17','18',
                       '19','20','21',
                       '22','23','24',
                       '25','26','27',
                       '28','29','30',
                       '31'],
                'time':['00:00','01:00','02:00',
                        '03:00','04:00','05:00',
                        '06:00','07:00','08:00',
                        '09:00','10:00','11:00',
                        '12:00','13:00','14:00',
                        '15:00','16:00','17:00',
                        '18:00','19:00','20:00',
                        '21:00','22:00','23:00'],
                'grid': "0.27/0.27",
                'area': "-32.0/-38.0/-29.0/-33.0",
                'format':'netcdf'},
            'ERA5_param_erg.nc')

# 2D Wave Spectra
"""
c2.retrieve('reanalysis-era5-complete', {
            	'class': "ea",
            	'dataset': "era5",
            	'date': "2015-03-01/to/2015-04-10",
            	'direction': "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24",
            	'domain': "g",
            	'expver': "1",
            	'frequency': "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30",
            	'param': "251.140",
            	'stream': "wave",
                'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
            	'type': "an",
            	'grid': "0.36/0.36",
            	'area': "-23.0/-42.0/-24.0/-41.0",
            	'format': "netcdf"},
            "ERA5_sfc_wspec_CF01.nc")
"""

