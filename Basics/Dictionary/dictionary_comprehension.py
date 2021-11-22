# dictionary comprehension = create dictionaries using an expression
#                               can replace for loops and certain lambda function

cities_in_F = {"New York": 32, "Boston":75, "Los Angeles": 100, "Chicago": 50}
weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}

#dictionary = {key: expression for (key, value) in iterables}
cities_in_C = {key: round((value - 32) * 5 / 9) for (key, value) in cities_in_F.items()}
print(cities_in_C)

#dictionry = {key: expression for (key, value) in iterable if conditional}
sunny_cities = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_cities)

#dictionry = {key: (if/else) for (key, value) in iterable}
desc_cities = {key: ("warm" if value >= 40 else "cold") for (key, value) in cities_in_F.items()}

#dictionry = {ke: function(value) for (key, value) in iterable}
def check_temp(value):
    if value >= 70:
        return "hot"
    elif 40 <= value <= 60:
        return "warm"
    else:
        return "cold"
desc_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(desc_cities)