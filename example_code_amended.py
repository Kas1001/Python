# (C) British Crown Copyright 2021, Met Office.
# Please see LICENSE for license details.
"""
This module contains some example code used for a code review exercise.
"""

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def create_anomaly_plot(infile,outpath):
    """
    Create a timeseries plot of anomaly values.
    Parameters
    ----------
    infile : string
        path and filename to a csv file containing monthly data
        five header rows columns.
        The fifth row has column headers 'Date_string' in the format %d/$m/%Y and
        'Mean_temperature' as floating point number
    output_path : string
        Where to send the output.
    """
    str2date = lambda x:datetime.strptime(x, '%d/%m/%Y')
    data_array = np.genfromtxt(infile,delimiter=',',names=True,skip_header=4,
                               converters={0: str2date}, encoding='utf-8',dtype=None)


    min_value = -35
    max_value = 50
    # Run a range check between -35 and 50 and set failing values to nan 
    for i in data_array:
        if i['Mean_temperature'] < min_value or i['Mean_temperature'] > max_value:
            i['Mean_temperature'] = np.nan

    years = np.array([x.year for x in data_array['Date_string']])
    months = np.array([x.month for x in data_array['Date_string']])
    temp_actual = data_array['Mean_temperature']
    ta6190 = np.empty(len(temp_actual))
    ta9120 = np.empty(len(temp_actual))

    # calculate climatology and anomaly values 1961-1990
    for month in range(1,13):
        #climatol6190 = np.mean(temp_actual[(years >= 1961) &
        #                               (years <= 1990) &
        #                               (months == month)])
        climatol6190 = np.nanmean(temp_actual[(years >= 1961) &
                                       (years <= 1990) &
                                       (months == month)])

        #climatol9120 = np.mean(temp_actual[(years >= 1991) &
        #                               (years <= 2020) &
        #                               (months == month)])
        climatol9120 = np.nanmean(temp_actual[(years >= 1991) &
                                       (years <= 2020) &
                                       (months == month)])
        
        ta6190[(months == month)] = temp_actual[(months == month)] - climatol6190
        ta9120[(months == month)] = temp_actual[(months == month)] - climatol9120

    
    # create bar plots
    barpositivecolor = "#E47452"
    barnegativecolor = "#007AA9"

    positivevals = ta6190 >=0
    colormap_dict = {True: barpositivecolor, False: barnegativecolor}
    colormap = list(map(lambda x:colormap_dict[x],positivevals))

    fig = plt.figure(figsize=(16,8))
    ax1 = fig.add_subplot(211)
    ax1.xaxis_date()
    
    ax1.set_title('Monthly mean temperature anomaly 1961-1990')
    ax1.set_ylabel('Monthly Mean Anomaly')
 
    p1 = plt.bar(data_array['Date_string'],ta6190, color=colormap,width=100)

    positivevals = ta9120 >=0
    colormap_dict = {True: barpositivecolor, False: barnegativecolor}
    colormap = list(map(lambda x:colormap_dict[x],positivevals))

    ax2 = fig.add_subplot(212)
    ax2.xaxis_date()
    
    ax2.set_title('Monthly mean temperature anomaly 1991-2020')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Monthly Mean Anomaly')
 
    p2 = plt.bar(data_array['Date_string'],ta9120, color=colormap,width=100)

    outfile = outpath + '/' + 'monthly_temperature_anomaly_test04.png'
    fig.savefig(outfile)

    
    return data_array, ta6190, ta9120

create_anomaly_plot('C:/Users/keith.stewart/Projects/VS_Projects/Python/test_monthly_mean_03.csv', 'C:/Users/keith.stewart/Projects/VS_Projects/Python')
