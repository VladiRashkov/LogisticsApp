# Use case 1:
# Input: RegisterCustomer user user_info 
# Output: Customer with username: steven1 and email: steven_smith@gmail.com has been registered!
# Input: CreatePackage id weight Sydney Melbourne date status
# Output: Package with id: 1; weight: 45kg; start location: Sydney, end location: Melbourne, status: unassigned has been created on 09/02 Friday @ 11:30!
# Input: ShowRoutes Sydney Melbourne date truck_status
# Output: 
# RouteID: #1 Brisbane (10/02 Saturday @ 06:00) → Sydney (10/02 Saturday @ 20:00) → Melbourne (11/02 Sunday @ 18:00)
# RouteID: #2 Sydney (12/02 Monday @ 06:00) → Melbourne (12/02 Monday @ 20:00) → Adelaide (13/02 Tuesday @ 15:00)
# Input: UpdateRoute id_package id_route
# Output: Package with id: 1 has been added to route with id: 1!
# Input: UpdatePackage id_package status ETA 
# Output: Package with id: 1 has new updates - status: assigned, ETA: Melbourne (11/02 Sunday @ 18:00)!

# Use case 2:
# Many packages with total weight of 23000kg have gathered in the hub in Alice Springs
# and an employee of the company uses the system to create a route that leaves on Sep 12th 06:00h with the following stops:
# -Alice Springs → Adelaide → Melbourne → Sydney → Brisbane
# The system determines the route distance to 4041km and calculates estimated arrival times for each of the locations based on a predefined average speed of 87km/h. 
# The employee then finds a free truck that meets the required range and capacity and proceeds to bulk assign the packages to the newly created route by using the route id and the packages’ ids.
# Input: CreateRoute date Alice Springs Adelaide Melbourne Sydney Brisbane
# Output:
# New route has been created:
# RouteID: #254 Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Melbourne (11/02 Sunday @ 18:00) -> Sydey (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
# Todal distance: 4041 km
# Start date: 10/02 Saturday @ 06:00
# Final ETA: 13/02 Tuesday @ 14:00
# Input: ShowTrucks capacity: 23000kg  max_range: 4041  truck_status date
# Output: 
# TruckID: 1036, capacity: 26000, max_range: 13000 km, status: available, date: 09/02 Friday @ 10:00
# TruckID: 1022, capacity: 37000, max_range: 10000 km, status: available, date: 11/02 Synday @ 12:00 
# TruckID: 1011, capacity: 42000, max_range: 8000 km, status: available, date: 08/02 Thursday @ 08:00 
# Input: UpdateRoute truck_id route_id
# Outpu: Truck with id: 1036 has been added to route with id: 245!
# Input: UpdateTruck truck_id status ETA
# Output: Truck with id: 1036 has new updates - status: unavailable, final ETA: Brisbane (13/02 Tuesday @ 14:00)!
# Input: UpdatePackage id_package status ETA 
# Output: Package with id: 24 has new updates - status: assigned, ETA: Adelaide (10/02 Saturday @ 20:00)!
# Input: UpdateRoute id_package id_route
# Output: Package with id: 24 has been added to route with id: 245!
# Input: ShowTrucks capacity: 23000kg  max_range: 4041  truck_status date
# Output: 
# TruckID: 1036, capacity: 26000, max_range: 13000 km, status: available, date: 09/02 Friday @ 10:00
# TruckID: 1022, capacity: 37000, max_range: 10000 km, status: available, date: 11/02 Synday @ 12:00 
# TruckID: 1011, capacity: 42000, max_range: 8000 km, status: available, date: 08/02 Thursday @ 08:00 
# Input: UpdateRoute truck_id route_id
# Outpu: Truck with id: 1036 has been added to route with id: 245!
# Input: UpdateTruck truck_id status ETA
# Output: Truck with id: 1036 has new updates - status: unavailable, final ETA: Brisbane (13/02 Tuesday @ 14:00)!
# Input: UpdatePackage id_package status ETA 
# Output: Package with id: 24 has new updates - status: assigned, ETA: Adelaide (10/02 Saturday @ 20:00)!
# Input: UpdateRoute id_package id_route
# Output: Package with id: 24 has been added to route with id: 245!

# Use case 3:
# Input: InfoRoutesInProgress date
# Output: List of routes:
# RouteID: #1 Brisbane (10/02 Saturday @ 06:00) → Sydney (10/02 Saturday @ 20:00) → Melbourne (11/02 Sunday @ 18:00)
# Delivery weight: 15000 kg
# Current ETA: Sydney (10/02 Saturday @ 20:00)

# Use case 4:
# Input: InfoPackagesUnassigned 
# Output: PackageID: 263, status: unassigned, location: Sydney, registered: 09/02 Friday @ 11:30

# Use case 5:
# Input: InfoPackage package_id date
# Output: 
# PackageID: 1;
# Registered: 09/02 Friday @ 11:30;
# Weight: 45kg; 
# Start location: Sydney, End location: Brisbane; 
# Current ETA: Melbourne (10/02 Saturday @ 18:00);
# Final ETA: Brisbane (11/02 Sunday @ 20:00).
