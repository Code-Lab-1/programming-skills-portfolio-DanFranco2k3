def describe_city(city, country='Philippines'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Manila')
print()
describe_city('Abu Dhabi', 'United Arab Emirates')
print()
describe_city('Cebu City')