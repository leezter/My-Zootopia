import json

# Step 1: Load the JSON file
def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

animals_data = load_data("animals_data.json")

# Step 2: Generate an inline HTML string
animals_info = ""
for animal in animals_data:
    animals_info += f"<strong>Name:</strong> {animal['name']} "

    if "diet" in animal["characteristics"]:
        animals_info += f"<strong>Diet:</strong> {animal['characteristics']['diet']} "

    if "locations" in animal and animal["locations"]:
        animals_info += f"<strong>Location:</strong> {animal['locations'][0]} "

    if "type" in animal["characteristics"]:
        animals_info += f"<strong>Type:</strong> {animal['characteristics']['type']} "

# Step 3: Load the HTML template
with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Step 4: Replace the placeholder __REPLACE_ANIMALS_INFO__ with inline formatted text
html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Step 5: Write the new inline-formatted HTML content to a file
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("? animals.html has been successfully formatted to match the given exercise!")
