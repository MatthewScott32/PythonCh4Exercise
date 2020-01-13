planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
print(planet_list)

planet_list.append("Saturn")
print(planet_list)

planet_list2 = ["Neptune", "Pluto"]

planet_list.extend(planet_list2)
print("Planet List Extended:" ,planet_list)

planet_list.insert(1, "Venus")
print(planet_list)

planet_list.insert(2, "Earth")
print(planet_list)

planet_list.insert(6, "Uranus")
print(planet_list)

rocky_planets = planet_list[0:4]
print(rocky_planets)

del planet_list[8]
print(planet_list)