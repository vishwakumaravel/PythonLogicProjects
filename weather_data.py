# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Vishwa Kumaravel
# Section: 579
# Assignment: 11.13
# Date: 11/7/2023
#
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

            if min_temp_str:
                min_temp.append(int(min_temp_str))

print(f"10-year maximum temperature: {int(max(max_temp))} F")
print(f"10-year minimum temperature: {int(min(min_temp))} F")
#print(months)

mont = str(input("Please enter a month: "))
month = int(datetime.strptime(mont, "%B").month)
year = int(input("Please enter a year: "))

temp_range = []
humid_range = []
wind_range = []
precip_range = []

for i in range(len(months)):
    if months[i] == month and years[i] == year:
        temp_range.append(av_temp[i])
        humid_range.append(humid[i])
        wind_range.append(wind_speed[i])
        precip_range.append(precip[i])

mean_temp = sum(temp_range)/len(temp_range) if len(temp_range) > 0 else 0
mean_hum = sum(humid_range)/len(humid_range) if len(humid_range) > 0 else 0
mean_wind = sum(wind_range)/len(wind_range) if len(wind_range) > 0 else 0
perc_precip = 0
for precipit in precip_range:
    if precipit != 0:
        perc_precip += 1
act_perc = (perc_precip/len(precip_range))*100 if len(precip_range) > 0 else 0

print(f"For {mont} {year}:")
print(f"Mean average daily temperature: {round(mean_temp, 1)} F")
print(f"Mean relative humidity: {round(mean_hum, 1)}%")
print(f"Mean daily wind speed: {mean_wind:0.2f} mph")
print(f"Percentage of days with precipitation: {round(act_perc, 1)}%")

        









