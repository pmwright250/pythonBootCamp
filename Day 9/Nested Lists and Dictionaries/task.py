capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

travel_log = {
    "France" : {
        "cities visited" : ["Paris","Lille","Dijon"],
        "total visits" : 12
    },
    "Germany" : ["Stuttgart", "Berlin"],
}

print(travel_log["France"]["cities visited"][1])

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])