import pandas


# data = pandas.read_csv("weather_data.csv")
# print(type(data)) # Data Frame Object
# print(type(data["temp"])) # Series Object
# print(data[data["temp"] == 24])
# data_dict = data.to_dict()
# print(data_dict)

# temp_series = data["temp"]
# temp_list = data["temp"].to_list()

# print(temp_list)
# print(f"Average Temperature: {round(sum(temp_list) / len(temp_list), 2)}")
# print(f"Max temperature: {temp_series.max()}")
# # We can also use simply 
# print(data["temp"].mean())

# Getting hold of a row in pandas with specific condition
# print(data[data.day == "Monday"])


# # Print the row of the day at which temperature was maximum
# day = data[data.temp == data.temp.max()]
# print(day)

# monday = data[data["day"] == "Monday"]
# # print(monday.condition)
# print("Temperature in celsius: ", end = "")
# print(int(monday.temp))
# print("Temperature in Fahrenheit: ", end = "")
# monday_temp_F = int(monday.temp) * (9 / 5) + 32
# print(monday_temp_F)

# data_dict = {
#     "name": ["Dean", "Sam", "Castiel", "Crowley", "Jody", "Bobby"],
#     "score": [100, 99, 100, 100, 90, 100]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("hunter_scores.csv")
