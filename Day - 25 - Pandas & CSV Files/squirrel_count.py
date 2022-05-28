import pandas

data = pandas.read_csv("squirrel_Data.csv")

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

num_of_cinnamon_squirrels = len(cinnamon_squirrels)
num_of_gray_squirrels = len(gray_squirrels)
num_of_black_squirrels = len(black_squirrels)

count_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_of_gray_squirrels, num_of_cinnamon_squirrels, num_of_black_squirrels]
}

# print(count_data)
count_data_frame = pandas.DataFrame(count_data)

count_data_frame.to_csv("squirrel_count.csv")