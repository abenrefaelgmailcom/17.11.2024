# # 1
# '''creating the dictionary'''
# israel_info = {
#     "name": "Israel",
#     "birth": 1948,
#     "population_millions": 9.3,
#     "capital": "Jerusalem",
#     "language": "Hebrew",
#     "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
#     "currency": "ILS",
#     "area_Kilometer": 22145,
#     "gdp_billion": 450
# }
# print(israel_info)
#
#
#
# capital = israel_info.get("capital")
# print("The capital of Israel is:", capital)
#
# keys = israel_info.keys()
# print("Keys:", list(keys))
#
# values = israel_info.values()
# print("Values:", list(values))
#
# for key, value in israel_info.items():
#     print(f"{key}: {value}")
#
# israel_info_copy = israel_info.copy()
# print("Copied dictionary:", israel_info_copy)
#
# gdp = israel_info_copy.pop("gdp_billion")
# print("Removed GDP:", gdp)
# print("Updated dictionary:", israel_info_copy)
#
# new_dict = dict.fromkeys(israel_info.keys(), None)
#
# '''getting values from the user'''
# new_dict["name"] = input("Enter country name: ")
# new_dict["birth"] = int(input("Enter year of birth: "))
# new_dict["population_millions"] = float(input("Enter population in millions: "))
# new_dict["capital"] = input("Enter capital city: ")
# new_dict["language"] = input("Enter main language: ")
# new_dict["cities"] = [
#     input("Enter city 1: "),
#     input("Enter city 2: "),
#     input("Enter city 3: ")
# ]
# new_dict["currency"] = input("Enter currency: ")
# new_dict["area_Kilometer"] = int(input("Enter area in kilometers: "))
# new_dict["gdp_billion"] = float(input("Enter GDP in billions: "))
#
# print("Updated dictionary:", new_dict)

#2

def length_of_last_word(s):
    """
    function that's return the length of the llast word on the string
    """
    """divide the string into words based on letter space"""
    words = s.split()  # wprd list
    """draw the last word and calculate its length"""
    return len(words[-1])

# דוגמאות לבדיקה
print(length_of_last_word("Hello World"))               # output: 5
print(length_of_last_word("   fly me   to   the moon  "))  # output: 4
print(length_of_last_word("luffy is still joyboy"))     # output: 6




