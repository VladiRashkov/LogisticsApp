Use case 1:
A customer visits the company office in Sydney on Oct 8th. 
They bring a package that needs to be delivered to Melbourne. 
An employee of the company records the customer’s contact info, weighs the package at 45kg and then checks for a suitable delivery route. 
The system reports that there are two routes:
-   Brisbane (Oct 10th 06:00h) → Sydney (Oct 10th 20:00h) → Melbourne (Oct 11th 18:00h)
-   Sydney (Oct 12th 06:00h) → Melbourne (Oct 12th 20:00h) → Adelaide (Oct 13th 15:00h)
Both routes' trucks have free capacity, and the employee suggests the first one, as the package will arrive one day earlier. 
The customer agrees and the employee uses the system to add the delivery package to the first route and to update the package’s expected arrival time to Oct 11th 18:00h.

1)	There is a route with those start and end points with an available truck assigned to it.

Input: RegisterCustomer username email 
Output: Customer with username: steven1 and email: steven_smith@gmail.com has been registered!

Input: CreatePackage Alice Springs Melbourne username weight
Output: Package with ID: 21 has been created! 

Input: ViewPackage IdPackage 
Output:
PackageID: 21
User: steven1
User email: steven_smith@gmail.com
Weight: 45 kg 
Start location: Alice Springs
End location: Melbourne 
Entry date: 09/02 Friday @ 11:30
Package status: unassigned
RouteID: Package is still unassigned.
TruckID: Package is still unassigned.
Final ETA: Package is still unassigned.

Input: ShowRoutes  
Output:
RouteID: 1
Route status: scheduled  (on route, arrived)
Route locations: Perth (15/02 Thursday @ 06:00) → Melbourne 16/02 Friday @ 22:00
Route total distance: 3509 km
Route start date: 15/02 Thursday @ 06:00
Route final ETA: 16/02 Friday @ 22:00
TruckID: 1011
Truck capacity: 10 115 kg
Truck status: available
PackagesID: 1, 5, 7, 8, 17, 15, 21
===============
RouteID: 2
Route status: scheduled 
Route locations: Alice Springs (16/02 Friday @ 06:00) → Melbourne 17/02 Saturday @ 07:00
Route total distance: 2255 km
Route start date: 16/02 Friday @ 06:00
Route final ETA: 17/02 Saturday @ 07:00
TruckID: 1026
Truck capacity: 21 115 kg
Truck status: available
PackagesID: 2, 6, 10, 11, 12
===============
RouteID: 3
Route status: scheduled 
Route locations: Bristbane (17/02 Saturday @ 06:00) → Adelaide 18/02 Sunday @ 04:00
Route total distance: 1927 km
Route start date: 17/02 Saturday @ 06:00
Route final ETA: 18/02 Sunday @ 04:00
TruckID: 1026
Truck capacity: 21 115 kg
Truck status: available
PackagesID: 2, 6, 10, 11, 12
===============

Input: ViewTruck TruckID
Output:
TruckID: 1026
Truck capacity: 21 115 kg
Truck max capacity: 27 000 kg
Truck max range: 8 000 km
Truck status: available
RouteID: 2
Route status: scheduled 
Route locations: Alice Springs (16/02 Friday @ 06:00) → Melbourne 17/02 Saturday @ 07:00
Route total distance: 2255 km
Route start date: 16/02 Friday @ 06:00
Route final ETA: 17/02 Saturday @ 07:00
PackagesID: 2, 6, 10, 11, 12

Input: AddPackageToRoute RouteId PackageId weight
Output: Package with ID: 21 has been added to route with ID: 2!

Input: ViewRoute RouteId
Output:
RouteID: 2
Route status: scheduled 
Route locations: Alice Springs (16/02 Friday @ 06:00) → Melbourne 17/02 Saturday @ 07:00
Route total distance: 2255 km
Route start date: 16/02 Friday @ 06:00
Route final ETA: 17/02 Saturday @ 07:00
TruckID: 1026
Truck capacity: 21 160 kg
Truck status: available
PackagesID: 2, 6, 10, 11, 12, 21

Input: UpdatePackage Assigned RouteId TruckId Eta
Output: Package with ID: 21 has been updated!

Input: ViewPackage PackageId 
Output:
PackageID: 21
User: steven1
User email: steven_smith@gmail.com
Weight: 45 kg 
Start location: Alice Springs
End location: Melbourne 
Entry date: 09/02 Friday @ 11:30
Package status: assigned
RouteID: 2
TruckID: 1026
Final ETA: 17/02 Saturday @ 07:00


Use case #2
Many packages with total weight of 23000kg have gathered in the hub in Alice Springs and an employee of the company uses the system to create a route that leaves on Sep 12th 06:00h with the following stops:
Alice Springs → Adelaide → Melbourne → Sydney → Brisbane
The system determines the route distance to 4041km and calculates estimated arrival times for each of the locations based on a predefined average speed of 87km/h. The employee then finds a free truck that meets the required range and capacity and proceeds to bulk assign the packages to the newly created route by using the route id and the packages’ ids.

2)	There is NO route with those start and end points with an available truck assigned to it.

Input: RegisterCustomer username email 
Output: Customer with username: steven1 and email: steven_smith@gmail.com has been registered!

Input: CreatePackage Sydney Melbourne username weight
Output: Package with ID: 21 has been created! 

Input: ViewPackage IdPackage 
Output:
PackageID: 21
User: steven1
User email: steven_smith@gmail.com
Weight: 45 kg 
Start location: Sydney
End location: Melbourne 
Entry date: 09/02 Friday @ 11:30
Package status: unassigned
RouteID: Package is still unassigned.
TruckID: Package is still unassigned.
Final ETA: Package is still unassigned.

Input: ShowRoutes  
Output:
RouteID: 1
Route status: scheduled  (on route, arrived)
Route locations: Perth (15/02 Thursday @ 06:00) → Melbourne 16/02 Friday @ 22:00
Route total distance: 3509 km
Route start date: 15/02 Thursday @ 06:00
Route final ETA: 16/02 Friday @ 22:00
TruckID: 1011
Truck capacity: 10 115 kg
Truck status: available
PackagesID: 1, 5, 7, 8, 17, 15, 21
===============
RouteID: 2
Route status: scheduled 
Route locations: Alice Springs (16/02 Friday @ 06:00) → Melbourne 17/02 Saturday @ 07:00
Route total distance: 2255 km
Route start date: 16/02 Friday @ 06:00
Route final ETA: 17/02 Saturday @ 07:00
TruckID: 1026
Truck capacity: 21 115 kg
Truck status: available
PackagesID: 2, 6, 10, 11, 12
===============
RouteID: 3
Route status: scheduled 
Route locations: Bristbane (17/02 Saturday @ 06:00) → Adelaide 18/02 Sunday @ 04:00
Route total distance: 1927 km
Route start date: 17/02 Saturday @ 06:00
Route final ETA: 18/02 Sunday @ 04:00
TruckID: 1026
Truck capacity: 21 115 kg
Truck status: available
PackagesID: 2, 6, 10, 11, 12
===============

Input: ShowHubs
Output: 
Adelaide weight: 15 650 kg
Adelaide PackageID: 78, 98, 74, 26, 75, 59, 4
===============
Melbourne weight: 21 788 kg
Melbourne PackageID: 78, 98, 74, 26, 75, 59, 4, 94, 26, 85, 49, 7
===============
Sydney weight: 10 101 kg
Sydney PackageID: 26, 75, 59, 4, 94, 26, 85, 49, 7
===============
Bristbane weight: 7 850 kg
Bristbane PackageID: 98, 74, 26, 75,
===============
Alice Springs weight: 30 945 kg
Alice Springs PackageID: 26, 85, 49, 7, 26, 75, 59, 4, 94, 26, 85, 49, 7
===============
Darwin weight: 39 466 kg
Darwin PackageID: 26, 85, 49, 7, 26, 75, 59, 4, 94, 26, 85, 49, 7
===============
Perth weight: 17 523 kg
Perth PackageID: 26, 75, 59, 4, 94, 26, 85, 49, 7

Input: CreateRoute  Alice Springs Adelaide Sydney Melbourne Brisbane
Output:
RouteID: 25
Route status: open
Route locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Sydney (11/02 Sunday @ 18:00) -> Melbourne (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
Route total distance: 4041 km
Route capacity: 30 945 kg
Route PackageID: 26, 85, 49, 7, 26, 75, 59, 4, 94, 26, 85, 49, 7
Route start date: 10/02 Saturday @ 06:00
Route final ETA: 13/02 Tuesday @ 14:00

Input: ShowTrucks
Output:
TruckID: 1007
Truck max capacity: 42 000 kg
Truck max range: 8 000 km
Truck status: available
===============
TruckID: 1012
Truck capacity: 37 000 kg
Truck max range: 10 000 km
Truck status: available
===============
TruckID: 1028
Truck capacity: 26 000 kg
Truck max range: 13 000 km
Truck status: available
===============

Input: AddTruckToRoute RouteId TruckId weight 
Output: Truck with ID: 1007 has been added to route with ID: 25!

Input: ViewRoute RouteId
Output:
RouteID: 25
Route status: scheduled 
Route locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Sydney (11/02 Sunday @ 18:00) -> Melbourne (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
Route total distance: 4041 km
Route start date: 10/02 Saturday @ 06:00
Route final ETA: 13/02 Tuesday @ 14:00
TruckID: 1007
Truck capacity: 30 945 kg
Truck status: available
PackagesID: 26, 85, 49, 7, 26, 75, 59, 4, 94, 26, 85, 49, 7

Input: AddPackageToRoute RouteId PackageId weight
Output: Package with ID: 21 has been added to route with ID: 25!

Input: ViewRoute RouteId
Output:
RouteID: 25
Route status: scheduled 
Route locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Sydney (11/02 Sunday @ 18:00) -> Melbourne (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)Route total distance: 2255 km
Route start date: 10/02 Saturday @ 06:00
Route final ETA: 13/02 Tuesday @ 14:00
TruckID: 1007
Truck capacity: 30 990 kg 
Truck status: available
PackagesID: 26, 85, 49, 7, 26, 75, 59, 4, 94, 26, 85, 49, 7, 21

Input: UpdatePackage Assigned RouteId TruckId Eta
Output: Package with ID: 21 has been updated!

Input: ViewPackage PackageId 
Output:
PackageID: 21
User: steven1
User email: steven_smith@gmail.com
Weight: 45 kg 
Start location: Sydney
End location: Melbourne 
Entry date: 09/02 Friday @ 11:30
Package status: assigned
RouteID: 25
TruckID: 1007
Final ETA: 13/02 Tuesday @ 14:00
Input: UpdateTruck Assigned RouteId PackageId weight
Output: Truck with ID: 1007 has been updated!

Input: ViewTruck TruckId
Output:
TruckID: 1007
Truck max capacity: 42 000 kg
Truck capacity: 30 990 kg
Truck max range: 8 000 km
Truck status: available
RouteID: 25
Route start date: 10/02 Saturday @ 06:00
Route final ETA: 13/02 Tuesday @ 14:00
PackagesID: 26, 85, 49, 7, 26, 75, 59, 4, 94, 26, 85, 49, 7, 21





















