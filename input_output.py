# USE CASES:

# Use case 1:
# A customer visits the company office in Sydney on Oct 8th. 
# They bring a package that needs to be delivered to Melbourne. 
# An employee of the company records the customer’s contact info, weighs the package at 45kg and then checks for a suitable delivery route. '
# The system reports that there are two routes:
# -	Brisbane (Oct 10th 06:00h) → Sydney (Oct 10th 20:00h) → Melbourne (Oct 11th 18:00h)
# -	Sydney (Oct 12th 06:00h) → Melbourne (Oct 12th 20:00h) → Adelaide (Oct 13th 15:00h)
# Both routes' trucks have free capacity, and the employee suggests the first one, as the package will arrive one day earlier. 
# The customer agrees and the employee uses the system to add the delivery package to the first route and to update the package’s expected arrival time to Oct 11th 18:00h.

# Input: RegisterCustomer username email 
# Output: Customer with username: steven1 and email: steven_smith@gmail.com has been registered!

# Input: CreatePackage weight Sydney Melbourne packagestatus
# Output: 
# PackageID: #1 
# Weight: 45 kg 
# Start location: Sydney
# End location: Melbourne 
# Package status: unassigned
# Entry date: 09/02 Friday @ 11:30

# Input: ShowRoutes Sydney Melbourne date capacity weight truckstatus
# Output: 
# RouteID: #1 
# Locations: Brisbane (10/02 Saturday @ 06:00) → Sydney (10/02 Saturday @ 20:00) → Melbourne (11/02 Sunday @ 18:00)
# Truck capacity: 10 100
# Truck status: available
# TruckID: #1005
# ==============
# RouteID: #2 
# Locations: Sydney (12/02 Monday @ 06:00) → Melbourne (12/02 Monday @ 20:00) → Adelaide (13/02 Tuesday @ 15:00)
# Truck capacity: 20 150
# Truck status: available
# TruckID: #1025

# Input: AddPakcageToRoute idpackage idroute
# Output: PackageID: #1 has been added to RouteID: #1!

# Input: UpdatePackage id status ETA 
# Output: 
# PackageID: #1
# Weight: 45 kg 
# Start location: Sydney 
# End location: Melbourne 
# Package status: assigned
# Entry date: 09/02 Friday @ 11:30
# Final ETA: 11/02 SUnday @ 17:00
# RouteID: #1

# Use case 2:
# Many packages with total weight of 23000kg have gathered in the hub in Alice Springs
# and an employee of the company uses the system to create a route that leaves on Sep 12th 06:00h with the following stops:
# -Alice Springs → Adelaide → Melbourne → Sydney → Brisbane
# The system determines the route distance to 4041km and calculates estimated arrival times for each of the locations based on a predefined average speed of 87km/h. 
# The employee then finds a free truck that meets the required range and capacity 
# and proceeds to bulk assign the packages to the newly created route by using the route id and the packages’ ids.

# Input: CreateRoute Alice Springs Adelaide Melbourne Sydney Brisbane
# Output:
# RouteID: #1
# Locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Melbourne (11/02 Sunday @ 18:00) -> Sydey (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
# Distance: 4041 km
# Start date: 10/02 Saturday @ 06:00
# Final ETA: 13/02 Tuesday @ 14:00

# Input: ShowTrucks capacity range truckstatus
# Output: 
# TruckID: 1036 
# Capacity: 26000 kg
# Range: 13000 km 
# Status: available
# ==============
# TruckID: 1022 
# Capacity: 37000 kg
# Range: 10000 km 
# Status: available
# ==============
# TruckID: 1011 
# Capacity: 42000 kg
# Range: 8000 km 
# Status: available
 
# Input: AddTruckToRoute truck_id route_id
# Outpu: TruckID: #1036 has been added to RouteID: #1!

# Input: UpdateTruck id status ETA
# Output:
# TruckID: 1036 
# Capacity: 26000 kg
# Range: 13000 km 
# Status: unavailable
# Final ETA: 17/02 Saturday @ 20:00
# RouteID: #1

# Input: AddPakcageToRoute idpackage idroute
# Output: PackageID: #24 has been added to RouteID: #1!

# Use case 3: not ready yet - changes to follow
# Use case 4: not ready yet - changes to follow
# Use case 5: not ready yet - changes to follow
