# command - show a delivery route to follow

# method that checks if the locations of the package match an existing route
# if a match is found - show options
# if no match use command createroute

# example 2: creating a random schedule 
# import random
# from datetime import datetime, timedelta
# from models.locations import Locations

# # locations = ['Adelaide', 'Melbourne', 'Sydney', 'Bristbane', 'Alice Springs', 'Darwin', 'Perth']

# cities = Locations.locations
    
# start_index = random.randint(0, 4)  
# end_index = random.randint(5, 6) + 1    
# cities = cities[start_index:end_index]

# num_cities = random.randint(2, len(cities))  
# num_routes = random.randint(1, 7)  
    
# scheduled_routes = []
# for _ in range(num_routes):
#     selected_cities = random.sample(population=cities, k=num_cities)
#     route = Route(*selected_cities)
#     scheduled_routes.append(route)

# for route in scheduled_routes:
#     print(route.route_info())