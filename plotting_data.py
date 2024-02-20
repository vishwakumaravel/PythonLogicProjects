# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: Lab 12.15
# Date: 11-20-2023

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
file_name = "WeatherDataCLL.csv"
dates = []
months = []
years = []
wind_speed = []
precip = []
humid = []
av_temp = []
max_temp = []
min_temp = []
with open(file_name, 'r') as file:
    next(file)
    for row in file:
        values = row.strip().split(',')
        date_str = values[0].strip()
        wind_speed_str = values[1].strip()
        precip_str = values[2].strip()
        humid_str = values[3].strip()
        av_temp_str = values[4].strip()
        max_temp_str = values[5].strip()
        min_temp_str = values[6].strip()
        if date_str:
            dates.append(str(date_str))          
            date_object = datetime.strptime(date_str, "%m/%d/%Y")
            months.append(int(date_object.month))
            years.append(int(date_object.year))

            if wind_speed_str:
                wind_speed.append(float(wind_speed_str))
            else:
                wind_speed.append(float(0))

            if precip_str:
                precip.append(float(precip_str))
            else:
                precip.append(float(0))

            if humid_str:
                humid.append(int(humid_str))
            else:
                humid.append(int(0))
            if av_temp_str:
                av_temp.append(int(av_temp_str))
            else:
                av_temp.append(int(0))

            if max_temp_str:
                max_temp.append(int(max_temp_str))
            else:
                max_temp.append(np.nan) 
            if min_temp_str:
                min_temp.append(int(min_temp_str))
            else: 
                min_temp.append(np.nan) 
    av_temps = []
    max_temps = []
    min_temps = []

    for month in sorted(set(months)):
        av_temp_month = []
        max_temp_month = []
        min_temp_month = []

        for i in range(len(months)):
            if months[i] == month:
                av_temp_month.append(av_temp[i])
                max_temp_month.append(max_temp[i])
                min_temp_month.append(min_temp[i])
        if av_temp_month:
            avg_temp = np.mean(av_temp_month)
        else: 
            None
        if max_temp_month:
            max_temp_month = max(max_temp_month) 
        else: 
            None
        if min_temp_month:
            min_temp_month = min(min_temp_month)
        else: 
            None

        av_temps.append(avg_temp)
        max_temps.append(max_temp_month)
        min_temps.append(min_temp_month)

#Plot 1: Max Temperature and Average Wind Speed
fig, ax1 = plt.subplots(figsize=(10, 6))
color = 'red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Max Temperature')
ax1.plot(dates, max_temp, color=color, label='Max Temperature')

ax2 = ax1.twinx()
color = 'blue'
ax2.set_ylabel('Average Wind Speed')
ax2.plot(dates, wind_speed, color=color, label='Average Wind Speed')
plt.title('Max Temperature and Average Wind Speed')

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
combined_handles = handles1 + handles2
combined_labels = labels1 + labels2
ax1.legend(combined_handles, combined_labels, loc='lower left')

plt.show()

# Plot 2: Histogram of average wind speed
plt.hist(wind_speed, np.arange(0, max(wind_speed)), edgecolor='black')
plt.xlabel('Average Wind Speed, mph')
plt.ylabel('Number of days')
plt.title('Histogram of Average Wind Speed')
#plt.ylim(0, 300)
plt.show()

# Plot 3: Precipitation vs Average Relative Humidity
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(humid, precip)
ax.set_xlabel('Precipitation (in)')
ax.set_ylabel('Average Relative Humidity (%)')
ax.set_title('Precipitation vs Average Relative Humidity')
plt.xlim(max(precip) + 2)
plt.show()

# Plot 4: Average, Highest, and Lowest Temperatures by Month
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.5
index = np.arange(len(sorted(set(months))))

ax.plot(index, max_temps, label='High T')
ax.plot(index, min_temps, label='Low T')
ax.legend()
ax.bar(index, av_temps, bar_width, label='Average Temperature')


ax.set_xlabel('Month')
ax.set_ylabel('Average Temperature, F')
ax.set_title('Average, Highest, and Lowest Temperatures by Month')
#ax.legend()

plt.show()
