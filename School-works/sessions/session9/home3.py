def listTrips(fileName,budget):
    ffile = open(fileName)
    l_trip = []
    for line in ffile:
        trip = line.split(';')
        trip_cost = float(trip[1])
        if trip_cost <= budget:
            l_trip.append(trip[0])
            
    return l_trip


b = float(input("Enter trip budget: "))

print("Suitable trips are:")
l = listTrips('trips.txt',b)
for e in l:
    print(e)