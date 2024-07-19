import pygame
import random
import math

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 8
COLS = 8

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 3
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold= True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_id = int(math.log2(self.value)) - 1
        if color_id >= len(self.COLORS):
            color_id = -1
        color = self.COLORS[color_id]
        return color
    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x + OUTLINE_THICKNESS, self.y + OUTLINE_THICKNESS, RECT_WIDTH - OUTLINE_THICKNESS, RECT_HEIGHT - OUTLINE_THICKNESS))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(text, (
                self.x + (RECT_WIDTH/2 - text.get_width()/2),
                self.y + (RECT_HEIGHT/2 - text.get_height()/2)
            )
        )
    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

    def set_p(self, ceil = False):
        if ceil:
            self.row = math.ceil(self.y/ RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)

def get_random_pos(tiles):
    row, col = None, None
    while True:
        row = random.randrange(0, ROWS )
        col = random.randrange(0, COLS )

        if f"{row}{col}" not in tiles:
            break
    return row, col

def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col - 1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        )
        ceil = True
    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x
        )
        ceil = False
    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL
        )
        ceil = True
    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y
        )
        ceil = False
    change = False
    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tile = sorted(tiles.values(), key= sort_func, reverse = reverse)
        for i, tile in enumerate(sorted_tile):
            if(boundary_check(tile)):
                continue

            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
                change = True
            elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                if(merge_check(tile, next_tile)):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tile.pop(i)
                    blocks.add(next_tile)
                change = True

            elif move_check(tile, next_tile):
                tile.move(delta)
                change = True

            else:
                continue
            tile.set_p(ceil)
            updated = True
        update_tiles(window, tiles, sorted_tile)
    return end_tiles(tiles, change)

def end_tiles(tiles, change):
    if len(tiles) == ROWS * COLS:
        return "Lost"
    if not change :
        return "continue"
    row, col = get_random_pos(tiles)
    rd = random.random();
    val = 2
    if rd >= 0.8:
        val = 4
    tiles[f"{row}{col}"] = Tile(val, row, col)
    return "continue"

def update_tiles(window, tiles, sorted_tile):
    tiles.clear()
    for tile in sorted_tile:
        tiles[f"{tile.row}{tile.col}"] = tile
    draw(window, tiles)
def generate_tile():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        rd = random.random();
        val = 2
        if rd >= 0.8:
            val = 4
        tiles[f"{row}{col}"] = Tile(val, row, col)
    return tiles

def draw_grid(window):

    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    for col in range (1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), 8)

def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)

    for tile in tiles.values():
        tile.draw(window)


    pygame.display.update()

def main(window):
    run = True
    clock = pygame.time.Clock()
    tiles = generate_tile()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type   == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tiles(window, tiles, clock, "left")
                if event.key == pygame.K_RIGHT:
                    move_tiles(window, tiles, clock, "right")
                if event.key == pygame.K_UP:
                    move_tiles(window, tiles, clock, "up")
                if event.key == pygame.K_DOWN:
                    move_tiles(window, tiles, clock, "down")
        draw(window, tiles)
    pygame.quit()



if __name__ == "__main__" :
    main(WINDOW)
