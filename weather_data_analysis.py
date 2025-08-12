weather = open("WeatherDataCLL.csv", 'r')
# making a list for each column
date = []
temp = []
dew = []
humid = []
wind = []
rain = []
max_temp = []
min_temp = []

lines = weather.readlines()
lines_updated = []
# going through each line in the file
# and removing rows with missing data
for i in range(len(lines)):
    line = lines[i].split(",")
    if "" not in line:
        lines_updated.append(lines[i])

del lines_updated[0] # removing header

for i in range(len(lines_updated)):
    line = lines_updated[i].split(",")
    # appending each data to a list matching its column
    date.append(line[0])
    dew.append(line[1])
    temp.append(line[2])
    humid.append(line[3])
    wind.append(line[4])
    max_temp.append(float(line[5]))
    min_temp.append(float(line[6]))
    rain.append(line[7])

weather.close()

maximum = max(max_temp) # get max temp
minimum = min(min_temp) # get min temp
print(f"10-year maximum temperature: {maximum:.0f} F")
print(f"10-year minimum temperature: {minimum:.0f} F")

month_user = input("Please enter a month: ")
year = input("Please enter a year: ")

month_num = {"January": "01", "February": "02", "March": "03",
             "April": "04", "May": "05", "June": "06", "July": "07",
             "August": "08", "September": "09", "October": "10",
             "November": "11", "December": "12"}

# making a list for each column
# that takes in data for the given month and year
data_temps = []
data_dews = []
data_humid = []
data_winds = []
data_rains = []

month = month_num[month_user]
# converting month to number format

for i in range(len(date)):
    dates = date[i].split("-") # make date into a list
    months = dates[1] # get month
    years = dates[0] # get year
    if month == months and year == years:
        data_temps.append(float(temp[i]))
        data_dews.append(float(dew[i]))
        data_humid.append(float(humid[i]))
        data_winds.append(float(wind[i]))
        data_rains.append(float(rain[i]))

def mean_values(list):
    mean = sum(list)/len(list)
    return mean

# find the average for most of the lists
avg_temp = mean_values(data_temps)
avg_dew = mean_values(data_dews)
avg_humid = mean_values(data_humid)
avg_wind = mean_values(data_winds)

# find percentage of days with rain
# count how many days we had rain, divide by total days
count = 0
for i in range(len(data_rains)):
    if data_rains[i] != 0.0:
        count += 1

avg_rain = (count/len(data_rains))*100

print(f"For {month_user} {year}: ")
print(f"Mean average daily temperature: {avg_temp:.1f} F")
print(f"Mean average daily dew point: {avg_dew:.1f} F")
print(f"Mean relative humidity: {avg_humid:.1f}%")
print(f"Mean daily wind speed: {avg_wind:.2f} mph")
print(f"Percentage of days with precipitation: {avg_rain:.1f}%")







