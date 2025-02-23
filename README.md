# Zootopia 🦊🐘🐼

## Overview

Zootopia is a Python-based project that fetches animal data from the **API Ninjas** database and dynamically integrates it into an HTML template. The generated webpage displays detailed information about various animals, making it an interactive and educational experience for users.

## Features

- Fetches animal data from the **API Ninjas** database.
- Parses and structures the data into HTML format.
- Automatically updates an HTML template with animal information.
- Generates a new webpage displaying animal details dynamically.

## Technologies Used

- **Python** (requests, os, dotenv)
- **API Ninjas** (for fetching animal data)
- **HTML** (template for displaying animal details)

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/deburic/My-Zootopia.git
cd My-Zootopia
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Set Up API Key

1. Get an API key from [API Ninjas](https://api-ninjas.com/).
2. Create a `.env` file in the project root and add:
   ```env
   API_KEY=your_api_key_here
   ```

## Usage

### Run the script

```sh
python animals_web_generator.py
```

### Expected Flow:

1. Enter an animal name when prompted.
2. The script fetches data from API Ninjas.
3. The updated `animals.html` file is created including HTML template and animals infos.
4. Open `animals.html` in a browser to view the information.

## Example Output

If you enter **"fox"**, the webpage will display:

```html
<li class="cards__item">
  <div class="card__title">Fox</div>
  <p class="card__text">
    <strong>Diet:</strong> Omnivore<br/>
    <strong>Location:</strong> North America<br/>
    <strong>Type:</strong> Mammal<br/>
  </p>
</li>
```

## Future Enhancements

- Implement a frontend UI for better interaction.
- Add search functionality to filter animals dynamically.
- Include images of animals fetched from an external API.

## Contributing

Feel free to fork the project, create a new branch, and submit a pull request. Contributions are welcome! 🎉

---

✨ \*\*Created by \*\***[Richard Nur](https://github.com/RichardNur)** ✨

