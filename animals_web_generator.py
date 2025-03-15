import json


def load_data(file_path):
    """ Reads a JSON file and returns the data as a Python list of dictionaries. """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal_obj):
    """ Converts a single animal dictionary into an HTML list item.
        Returns formatted html string containing the animal's name, 
        diet, location, and type. """
    output = '<li class="cards__item">\n'
    output += f'    <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '    <p class="card__text">\n'

    if "diet" in animal_obj["characteristics"]:
        output += f'        <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'        <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "type" in animal_obj["characteristics"]:
        output += f'        <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '    </p>\n'
    output += '</li>\n'
    return output


def main():
    """ Reads animal data from json, processes it into html and writes the 
    final HTML output to a file. """
    animals_data = load_data("animals_data.json")

    animals_info = '<ul class="cards">\n'
    for animal in animals_data:
        animals_info += serialize_animal(animal)
    animals_info += "</ul>\n"

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)


if __name__ == "__main__":
    main()