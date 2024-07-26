# # PRINT THE TEMPERATURES WITHOUT PANDA
# #
# # import csv
# #
# # with open("weather_data.csv") as weather_data_file:
# #     weather_data = csv.reader(weather_data_file)
# #     temperatures = []
# #     for row in weather_data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # PRINT THE TEMPERATURES WITH PANDA
#
# import pandas
#
# weather_data = pandas.read_csv("weather_data.csv")
# temp_list = weather_data["temp"].to_list()
#
# print(weather_data["temp"].max())
#
# # Get data in columns
# print(weather_data["condition"])
# print(weather_data.condition)
#
# # Get data in rows
# print(weather_data[weather_data.day == "Monday"])
# print(weather_data[weather_data.temp == weather_data.temp.max()])
#
# monday = weather_data[weather_data.day == "Monday"]
# print(monday.condition)
# print(monday.temp*1.8 + 32)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# student_data = pandas.DataFrame(data_dict)
# student_data.to_csv("student_data.csv")
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colour_list = squirrel_data["Primary Fur Color"]
counted_list = fur_colour_list.value_counts()
squirrel_colour_count = pandas.DataFrame(counted_list)
squirrel_colour_count.to_csv("Squirrel Colour Count")
