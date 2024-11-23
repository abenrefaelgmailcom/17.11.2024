# 1
'''creating the dictionary'''
israel_info = {
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_Kilometer": 22145,
    "gdp_billion": 450
}
print(israel_info)



capital = israel_info.get("capital")
print("The capital of Israel is:", capital)

keys = israel_info.keys()
print("Keys:", list(keys))

values = israel_info.values()
print("Values:", list(values))

for key, value in israel_info.items():
    print(f"{key}: {value}")

israel_info_copy = israel_info.copy()
print("Copied dictionary:", israel_info_copy)

gdp = israel_info_copy.pop("gdp_billion")
print("Removed GDP:", gdp)
print("Updated dictionary:", israel_info_copy)

new_dict = dict.fromkeys(israel_info.keys(), None)

'''getting values from the user'''
new_dict["name"] = input("Enter country name: ")
new_dict["birth"] = int(input("Enter year of birth: "))
new_dict["population_millions"] = float(input("Enter population in millions: "))
new_dict["capital"] = input("Enter capital city: ")
new_dict["language"] = input("Enter main language: ")
new_dict["cities"] = [
    input("Enter city 1: "),
    input("Enter city 2: "),
    input("Enter city 3: ")
]
new_dict["currency"] = input("Enter currency: ")
new_dict["area_Kilometer"] = int(input("Enter area in kilometers: "))
new_dict["gdp_billion"] = float(input("Enter GDP in billions: "))

print("Updated dictionary:", new_dict)

#2
#a
s = "Hello World"
words = s.split()  # ['Hello', 'World']
last_word = words[-1]  # 'World'
result = len(last_word)  # 5

#b
s = "   fly me   to   the moon  "
words = s.split()  # ['fly', 'me', 'to', 'the', 'moon']
last_word = words[-1]  # 'moon'
result = len(last_word)  # 4

#c
s = "luffy is still joyboy"
words = s.split()  # ['luffy', 'is', 'still', 'joyboy']
last_word = words[-1]  # 'joyboy'
result = len(last_word)  # 6
