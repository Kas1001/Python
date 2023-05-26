from itinerary import *

#trip = Itinerary.from_locations(maracaibo, rotterdam, stockholm)

#print(trip)

#print(trip.locations)

#print(trip.origin)

#print(trip.destination)

"""trip.add(cape_town)
trip.add(hong_kong)

trip.remove("Stockholm")

trip.truncate_at("Rotterdam")

print(trip)"""

trip = Itinerary.from_locations(rotterdam, rotterdam)

print(trip)