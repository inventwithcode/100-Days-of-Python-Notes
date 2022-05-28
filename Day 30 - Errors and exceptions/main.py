# # Errors and exceptions
# try:
#     data = open("file.txt", "r")
#     some_dictionary = {"some_key": "some_value"}
#     # print(some_dictionary["non_existing_key"])
#     print(some_dictionary["some_key"])
# except FileNotFoundError:
#     print("File was not found!")
#     data = open("file.txt", "w")
#     data.write("Something")
# except KeyError as error:
#     print(f"The key {error} doesn't exist!")
# else:
#     print("try successful")
# finally:
#     print(data.read())
#     print("File was closed")
#     data.close()

height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kg: "))
bmi = weight / height ** 2
if height > 3:
    raise ValueError("Look at your height, you ain't human!")
if weight > 300:
    raise ValueError(f"Your weight is {weight}, What the hell? What are you?r")
print(bmi)
