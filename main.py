import random
from functions import pretty_print, insert_2_or_4, get_number_from_index, \
get_empty_list, get_index_from_number, is_there_an_empty_cell, move_left, move_right, move_up, move_down, \
is_there_a_way_out
import pygame
import sys

def draw_interface():
    pygame.draw.rect(screen, TEAL, TOP_PANEL) #выводим на экран прямоугольник с игрой
    font = pygame.font.SysFont("Calibri", 70)
    pretty_print(l)
    for row in range(4):
        for column in range(4):
            value = l[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * BLOCK_SIDE + MARGIN * (column + 1)
            h = row * BLOCK_SIDE + MARGIN * (row + 1) + 110
            pygame.draw.rect(screen, COLORS[value], (w, h, BLOCK_SIDE, BLOCK_SIDE))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (BLOCK_SIDE - font_w) / 2
                text_y = h + (BLOCK_SIDE - font_h) / 2
                screen.blit(text, (text_x, text_y))


l = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

COLORS = {
    0: (204, 255, 255),
    2: (255, 255, 204),
    4: (255, 204, 253),
    8: (255, 153, 51),
    16: (204, 102, 51),
    32: (255, 153, 102),
    64: (255, 153, 102),
    128: (255, 153, 102),
    256: (255, 153, 102),
    512: (255, 153, 102),
    1024: (255, 153, 102),
    2048: (255, 153, 102),

}

TEAL = (0, 128, 128)
AZURE = (204, 255, 255)
BLACK = (0, 0, 0)
BLOCKS = 4
BLOCK_SIDE = 110
MARGIN = 10
WIDTH = BLOCKS * BLOCK_SIDE + MARGIN * (BLOCKS + 1)
HEIGHT = BLOCKS * BLOCK_SIDE + MARGIN * (BLOCKS + 1) + 110
TOP_PANEL = pygame.Rect(0,0,WIDTH,110)

l[1][3] = 2
l[2][2] = 4
print(get_empty_list(l))
pretty_print(l)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
draw_interface()
pygame.display.update()

while is_there_an_empty_cell(l) or is_there_a_way_out(l):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                l = move_left(l)
            elif event.key == pygame.K_RIGHT:
                l = move_right(l)
            elif event.key == pygame.K_UP:
                l = move_up(l)
            elif event.key == pygame.K_DOWN:
                l = move_down(l)


            #input()
            empty = get_empty_list(l)
            random.shuffle(empty)
            random_empty_cell = empty.pop()  # удаляем и возвращаем последний элемент уже перемешанного списка(заполненного номерами пустых  ячеек)
            x, y = get_index_from_number(random_empty_cell)
            l = insert_2_or_4(l, x, y)
            print(f'Мы заполнили элемент под номером {random_empty_cell}')
            draw_interface()
            pygame.display.update()

