# Lists
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
attractions = [[] for destination in destinations]

# Test Traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Index of destinations function
def get_destinations_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# Traveler location function
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destinations_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

# Adding attractions to the list
def add_attraction(destination, attraction):
  destination_index = get_destinations_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Travelers places of interest
def find_attractions(destination, interests):
  destination_index = get_destinations_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      count_of_interests = attraction_tags.count(interest)
      if count_of_interests > 0:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

# Atractions for Traveler
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": the "
  for attraction in traveler_attractions:
    interests_string += attraction
    if len(traveler_attractions) > 1:
      interests_string += ", the "
    interests_string += "."
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)
