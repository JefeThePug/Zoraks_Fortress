# Zorak's Fortress

Zorak's Fortress is a text adventure game designed for the Practical Python server. Built with Python and Flask, this Interactive Fiction (I.F.) game allows players to explore a mysterious land filled with forests, villiages, underground caves, volcanic ruins, and cemetaries. They make choices and engage in a narrative experience through command inputs. **This project is currently a work in progress.**

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Structure](#game-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Interactive Gameplay**: Engage with the story through text-based commands.
- **Dynamic Command Parsing**: Use a variety of verbs and synonyms to navigate the game world.
- **Custom-Made Parser**: The command parser is entirely custom-built to enhance the gameplay experience.
- **Session Management**: Track player progress with session cookies.
- **Custom Maps**: Explore the world with a visual representation of your journey that updates itself as you visit spaces on the map.
- **User  Notes**: Take personal notes to assist with your adventure.
- **Responsive Design**: Play directly in your browser.

## Installation

To install Zorak's Fortress, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/JefeThePug/Zoraks_Fortress.git
   cd Zoraks_Fortress
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000` to start playing!

## Usage

Once the game is running, you can start interacting with the story by entering commands in the text input field. Common commands include:

- `go north`
- `look around`
- `take item`
- `open door`
- `talk to character`

Explore the different areas of the map, interact with objects, collect key components, and uncover the story as you progress.

## Game Structure

The game is structured into several key components:

- **`zorakapp/__init__.py`**: Initializes the Flask application and database.
- **`zorakapp/action_manager.py`**: Manages game actions based on user input.
- **`zorakapp/parser.py`**: A completely custom-made parser that processes user commands and extracts verbs, objects, and prepositions.
- **`zorakapp/views.py`**: Defines the routes and rendering logic for the web application.
- **`templates/`**: Contains HTML templates for rendering different game views.
- **`static/`**: Holds custom map images and sound files for an immersive experience.

## Contributing

Contributions to Zorak's Fortress are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Create a pull request describing your changes.

Please ensure your code follows the existing style and is well-documented.

## License

This Boggle game implementation is open-source and available for personal or educational use.

---

Enjoy your adventure in Zorak's Fortress! If you encounter any issues or have suggestions, feel free to open an issue on GitHub.
