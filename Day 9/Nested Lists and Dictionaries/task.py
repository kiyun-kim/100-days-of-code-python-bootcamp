capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print out "Lille" from the nested List called travel_log
print(travel_log["France"][1])

# print "D" from the list nested_list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# print "Tokyo" from the list travel_city_log
travel_city_log = {
    "Korea": {
        "num_times_visited": 12,
        "cities_visited": ["Seoul", "Busan", "Daejeon"]
    },
    "Japan": {
        "num_times_visited": 8,
        "cities_visited": ["Tokyo", "Osaka", "Fukuoka"]
    },
}

print(travel_city_log["Japan"]["cities_visited"][0])