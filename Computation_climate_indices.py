import pandas as pd
import numpy as np
import os

# Directories containing the data files
tmin_dir = '/Users/loverighteous1/Desktop/MasterThesisData/tmin' 
tmax_dir = '/Users/loverighteous1/Desktop/MasterThesisData/tmax'          
precip_dir = '/Users/loverighteous1/Desktop/MasterThesisData/CPC_total_pre_day_0.5x0.5_1979-2021_']

# Loop through each file in the directory
for file_name in os.listdir(tmin_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(tmin_dir, file_name)
        tmin_data = pd.read_csv(file_path, parse_dates=['date'])
        tmin_data = tmin_data.sort_values('date')
        tmin_data.set_index('date', inplace=True)
        
for file_name in os.listdir(tmax_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(tmax_dir, file_name)
        tmax_data = pd.read_csv(file_path, parse_dates=['date'])
        tmax_data = tmax_data.sort_values('date')
        tmax_data.set_index('date', inplace=True)


for file_name in os.listdir(precip_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(precip_dir, file_name)
        precip_data = pd.read_csv(file_path, parse_dates=['date'])
        precip_data = precip_data.sort_values('date')
        precip_data.set_index('date', inplace=True)
        
        










###### Indices computation
def tmin(mindata):
    # Calculate TN10P
    tn10 = mindata['tmin'].quantile(0.10)
    cold_nights = mindata['tmin'] < tn10
    TN10P = cold_nights.sum() / len(mindata) * 100
    return TN10P

def tmax(maxdata):
    # Calculate TX90P
    tx90 = maxdata['tmax'].quantile(0.90)
    warm_days = maxdata['tmax'] > tx90
    TX90P = warm_days.sum() / len(maxdata) * 100
    return TX90P

def cwd(precip):
    # Calculate CWD
    wet_days = precip['precip'] > 1
    consecutive_wet_days = (wet_days != wet_days.shift()).cumsum()
    wet_day_streaks = wet_days.groupby(consecutive_wet_days).cumsum()
    CWD = wet_day_streaks.max()
    return CWD

def R95PTOT(precip):
    # Calculate R95PTOT
    r95 = precip['precip'].quantile(0.95)
    extreme_wet_days = precip['precip'] > r95
    R95PTOT = precip.loc[extreme_wet_days, 'precip'].sum()
    return R95PTOT