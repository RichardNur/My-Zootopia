import data_fetcher

def read_animal_info(animal, data):
    """
    Generates an HTML-formatted string containing animal details.

    :param animal: The name of the animal.
    :param data: The dictionary response from the API.
    :return: A formatted string with animal details.
    """
    animal_info = ""

    if not data:
        return f"The animal {animal} doesn't exist in the Database."

    for info in data:
        try:
            name, taxonomy, locations, characteristics = info.values()

            animal_info += f"\n"
            animal_info += f'<li class="cards__item">\n'
            animal_info += f'<div class="card__title">{name}</div>\n'
            animal_info += f'<p class="card__text">\n'
            animal_info += f'<strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
            animal_info += f'<strong>Location:</strong> {locations[0]}<br/>\n'
            animal_info += f'<strong>Type:</strong>{characteristics["type"]}l<br/>\n'
            animal_info += f'</p>\n'
            animal_info += "</li>\n"
        except KeyError:
            animal_info += f'</p>\n'
            animal_info += "</li>\n"
            continue
    return animal_info

def read_html_template(path):
    """
    Reads an HTML template file.

    :params: filepath to html-template.
    :return: HTML content as a string
    """
    try:
        with open(path, 'r') as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error File '{path}' not found.")
        return ""

def create_animals_info_html(text_to_replace, template, animal_info):
    """
    Inserts animal information into the HTML template.

    :param text_to_replace: The placeholder text in the template.
    :param template: The HTML template content.
    :param animal_info: The formatted animal info string.
    :return: Updated HTML string.
    """
    if text_to_replace not in template:
        print(f"Warning: '{text_to_replace}' not found in the template. No changes made.")
        return template  # Return unmodified template

    return template.replace(text_to_replace, animal_info)

def write_animals_html(new_path, content):
    """
    :param new_path: File path for the new HTML file.
    :param content: HTML content to be written.
    :return: True if successful, False otherwise.
    """
    try:
        with open(new_path, 'w') as file:
            file.write(content)
            return True

    except (FileNotFoundError, IOError) as e:
        print(f"Error writing to file '{new_path}': {e}")
        return False

def main():
    """
    Fetch animal data, update the HTML template, and save the results in new file.
    """

    # Get the animal to be displayed:
    animal = input("Enter the animal you want to load the content for (in html): ").strip()

    # Load animal data
    data = data_fetcher.load_data(animal)
    # Load HTML template
    html_template = read_html_template('animals_template.html')

    # Process and save HTML file
    animal_info = read_animal_info(animal, data)
    new_html = create_animals_info_html('__REPLACE_ANIMALS_INFO__', html_template, animal_info)
    if write_animals_html("animals.html", new_html):
        print("HTML file updated successfully!")
    else:
        print("Failed to update HTML file.")


if __name__ == "__main__":
    main()