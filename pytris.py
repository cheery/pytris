from pygame import mixer
import pygame
import sys
import random

pygame.init()
mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tetris shapes
SHAPES = [
    # T Shape
    ['.OOO.',
     '..O..',
     '.....',
    ],
    # J Shape
    ['.O...',
     '.OOO.',
     '.....',
    ],
    # L Shape
    ['...O.',
     '.OOO.',
     '.....',
    ],
    # S Shape
    ['..OO.',
     '.OO..',
     '.....',
    ],
    # Z Shape
    ['.OO..',
     '..OO.',
     '.....',
    ],
    # O Shape
    ['.OO..',
     '.OO..',
     '.....',
    ],
    # I Shape
    ['.....',
     'OOOO.',
     '.....',
    ],
]

def rotate(shape):
    return [''.join([shape[y][x] for y in range(len(shape))])
            for x in range(len(shape[0]) - 1, -1, -1)]

def check_collision(grid, tetromino, position):
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell == "O":
                new_x, new_y = position[0] + x, position[1] + y
                if new_x < 0 or new_x >= GRID_WIDTH:  # Check left and right boundaries
                    return True
                try:
                    if grid[new_y][new_x] != ".":
                        return True
                except IndexError:
                    return True
    return False

def clear_rows(grid):
    full_rows = []
    for y, row in enumerate(grid):
        if all(cell != "." for cell in row):
            full_rows.append(y)
    
    if full_rows:
        for y in full_rows:
            del grid[y]
            grid.insert(0, ["."] * GRID_WIDTH)
    return len(full_rows)

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

    def draw(self, screen):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell == "O":
                    pygame.draw.rect(screen, WHITE,
                                     pygame.Rect((self.x + x) * GRID_SIZE,
                                                 (self.y + y) * GRID_SIZE,
                                                 GRID_SIZE, GRID_SIZE), 0)

    def move(self, dx, dy, grid):
        new_position = (self.x + dx, self.y + dy)
        if not check_collision(grid, self.shape, new_position):
            self.x, self.y = new_position
            return True
        return False

    def rotate(self, grid):
        new_shape = rotate(self.shape)
        if not check_collision(grid, new_shape, (self.x, self.y)):
            self.shape = new_shape


class GameGrid:
    def __init__(self):
        self.grid = [["."] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    def add_tetromino(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell == "O":
                    self.grid[tetromino.y + y][tetromino.x + x] = "O"

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == "O":
                    pygame.draw.rect(screen, WHITE,
                                     pygame.Rect(x * GRID_SIZE,
                                                 y * GRID_SIZE,
                                                 GRID_SIZE, GRID_SIZE), 0)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    grid = GameGrid()

    key_repeat_counters = {
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0,
        pygame.K_DOWN: 0,
    }
    key_repeat_threshold = 150

    tetromino = Tetromino(GRID_WIDTH // 2, 0, random.choice(SHAPES))
    fall_time = 0
    fall_speed = 500  # ms
    last_fall_time = pygame.time.get_ticks()

    mixer.music.load('background_music.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.05)

    while True:
        screen.fill(BLACK)
        current_time = pygame.time.get_ticks()
        fall_time += current_time - last_fall_time
        last_fall_time = current_time

        keys = pygame.key.get_pressed()

        for key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
            if keys[key]:
                if key_repeat_counters[key] == 0 or key_repeat_counters[key] >= key_repeat_threshold:
                    if key == pygame.K_LEFT:
                        tetromino.move(-1, 0, grid.grid)
                    elif key == pygame.K_RIGHT:
                        tetromino.move(1, 0, grid.grid)
                    elif key == pygame.K_DOWN:
                        tetromino.move(0, 1, grid.grid)
                key_repeat_counters[key] += clock.get_time()
            else:
                key_repeat_counters[key] = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tetromino.rotate(grid.grid)

        if fall_time > fall_speed:
            if not tetromino.move(0, 1, grid.grid):
                grid.add_tetromino(tetromino)
                cleared_rows = clear_rows(grid.grid)
                tetromino = Tetromino(GRID_WIDTH // 2, 0, random.choice(SHAPES))
                if check_collision(grid.grid, tetromino.shape, (tetromino.x, tetromino.y)):
                    # Game over, reset grid and tetromino
                    grid = GameGrid()
            fall_time = 0

        tetromino.draw(screen)
        grid.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
