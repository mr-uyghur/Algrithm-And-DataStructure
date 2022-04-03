# use linear search and apply it to more complex algorithms

# For each element in the searchList
# if element equal target value then
# Add its index to a list of occurrences
# if the list of occurrences is empty
# raise ValueError
# otherwise
# return the list occurrences

# Search list and target value
tour_locations = ["New York City", "Los Angeles", "Bangkok",
                  "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

# Linear Search Algorithm


def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
    if matches:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))


# Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
