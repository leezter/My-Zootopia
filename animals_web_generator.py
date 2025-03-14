import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

animals_data = load_data("animals_data.json")

animals_info = '<ul class="cards">\n'


for animal in animals_data:
    animals_info += '    <li class="cards__item">\n'
    animals_info += f'        <div class="card__title">{animal["name"]}</div>\n'
    animals_info += '        <p class="card__text">\n'

    if "diet" in animal["characteristics"]:
        animals_info += f'            <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        animals_info += f'            <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in animal["characteristics"]:
        animals_info += f'            <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    animals_info += '        </p>\n'  
    animals_info += '    </li>\n'  

animals_info += "</ul>\n"  

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# animals.html has now been updated with improved card item")

