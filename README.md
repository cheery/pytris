
# Pytris - A Simple Tetris Game in Python and Pygame

Pytris is a basic implementation of the classic Tetris game using Python and the Pygame library. The game features simple graphics, controls, and procedurally generated background music.

## Requirements

- Python 3.7 or higher
- Pygame
- pydub
- FFmpeg

## Installation

1. Install Python from the official website: https://www.python.org/downloads/
2. Install Pygame, pydub, and FFmpeg using the following commands:

```
pip install pygame
pip install pydub
```


Follow the instructions for your platform to install FFmpeg: https://github.com/jiaaro/pydub#dependencies

## Usage

### Generating Background Music

1. Run the `generate_music.py` script to create a background music file:


```
python generate_music.py
```

This will generate an MP3 file named `background_music.mp3` that will be used as background music for the game.

### Running the Game

1. Run the `pytris.py` script to start the game:

```
python pytris.py
```

2. Use the arrow keys to control the falling tetrominoes:

   - Left arrow: Move left
   - Right arrow: Move right
   - Up arrow: Rotate
   - Down arrow: Soft drop

3. The game ends when the tetrominoes reach the top of the screen.

## Contributing

Feel free to contribute to this project by submitting issues, suggesting improvements, or creating pull requests. We appreciate any feedback and help to make the game better.

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Make your changes or additions in the new branch.
4. Submit a pull request with a clear description of your changes and reference any related issues.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- The Pygame library for providing a simple and efficient way to build the game.
- The pydub library for enabling procedural music generation.
- OpenAI's GPT-4 for assisting in the development process.

## Disclaimer

This project is not affiliated with, endorsed by, or sponsored by the Tetris brand or its trademark owners.

