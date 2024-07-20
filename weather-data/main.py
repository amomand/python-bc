# PRINT THE TEMPERATURES WITHOUT PANDA
#
# import csv
#
# with open("weather_data.csv") as weather_data_file:
#     weather_data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# PRINT THE TEMPERATURES WITH PANDA

import pandas

weather_data = pandas.read_csv("weather_data.csv")
print(weather_data["temp"])
