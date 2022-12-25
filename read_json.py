"""
This program demonstrates how to read and parse a JSON file using Python's standard libraries.

Specifically, this program reads a JSON file named `apple-varieties.json` and prints the attributes about each apple like
the name, color, flavor all fields in a table-formatted output.
"""

import json

# Load the apple types from a local JSON file
with open('apple-varieties.json', 'r') as apple_varieties_json_file:
    apple_varieties = json.load(apple_varieties_json_file)

# Print the header
print('{:<20}{:<20}{:<30}{:<20}'.format('Name', 'Color', 'Flavor', 'Origin'))

# Print the rows of data
for apple_variety in apple_varieties:
    name = apple_variety['name']
    color = apple_variety['color']
    flavor = apple_variety['flavor']
    origin = apple_variety['origin']

    print('{:<20}{:<20}{:<30}{:<20}'.format(name, color, flavor, origin))