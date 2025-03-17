capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# travel_log = {
#     "France": ["Paris","Dijon", "Lille"],
#     "Germany" : ["Stuttgart", "Berlin"]
# }

#print(travel_log["France"][2])

nested_list = ["A","B", ["C","D"]]

#print(nested_list[2][1])


travel_log = {
    "France": {
        "total_visits": 12,
        "Cities_visited":["Paris","Dijon", "Lille"]
    },
    "Germany" : {
        "total_vists": 5,
        "cities_visited": ["Berlin", "Stuttgart"]
    }
}

print(travel_log["Germany"]["cities_visited"][1])