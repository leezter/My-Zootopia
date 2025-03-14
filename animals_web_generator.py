import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
print(animals_data)


for animal in animals_data:
    print(f"Name: {animal['name']}")

    # Check if "diet" exists in "characteristics" before printing
    if "diet" in animal["characteristics"]:
        print(f"Diet: {animal['characteristics']['diet']}")

    # Check if "locations" exist and is not empty before printing
    if "locations" in animal and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")  # Print the first location

    # Check if "type" exists in "characteristics" before printing
    if "type" in animal["characteristics"]:
        print(f"Type: {animal['characteristics']['type']}")

    print()  # Print a blank line for better readability
