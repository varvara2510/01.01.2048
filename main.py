import random
from functions import *
import pygame
import sys
from database import get_best, cur, insert_result


GAMERS_DB = get_best()

def draw_top_gamers():
    font_top = pygame.font.SysFont("simsun", 30)    #шрифт, отвечающий за главную запись
    font_gamer = pygame.font.SysFont("simsun", 24)  #шрифт, отвечающий за размер отрисовки имен игроков
    text_head = font_top.render("Best tries: ", True, COLOR_TEXT)   #заголовки
    screen.blit(text_head, (250, 5))   #прикрепляем текст к экрану
    for index, gamer in enumerate(GAMERS_DB):  #обходим коллекцию лучших результатов, полученную из функции get_best
        name, score = gamer
        s = f'{index+1}.{name} - {score}'
        #выводим номер строки (индекс + 1), далее ставим точку, далее выводим имя игрока и через "-" указываем сколько очков он набрал
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (250, 30 + 25*index)) #делаем шаг 20*index, чтобы строки с лучшими игроками не наслаивались друг на друга
        print(index,name, score)                     #получаем индекс элементаиз списка(он отсортирован от лучшего результата к худшему),  а также имя и результат игрока

def draw_interface(score, delta=0):          #функция, которая рисует интерфейс
    pygame.draw.rect(screen, WHITE_MINT, TOP_PANEL) #выводим на экран прямоугольник с игрой
    font = pygame.font.SysFont("simsun", 70)
    font_score = pygame.font.SysFont("simsun", 50)
    font_delta = pygame.font.SysFont("simsun", 25)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score} ", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35)) #прикрепляем текст и его координаты, чтобы он отображался в прямоугольнике над самой игрой
    screen.blit(text_score_value, (175, 35))
    if delta > 0:
        text_delta = font_score.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_delta, (170, 65))
    pretty_print(l)
    draw_top_gamers()
    for row in range(4):      #создание интерфейса
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

COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (204, 255, 255),
    2: (255, 99, 71),
    4: (255, 140, 0),
    8: (255, 215, 0),
    16: (154, 205, 50),
    32: (30, 144, 255),
    64: (0, 0, 205),
    128: (128, 0, 128),
    256: (218, 165, 32),
    512: (160, 82, 45),
    1024: (233, 150, 122),
    2048: (255, 160, 122),

}

WHITE_MINT = (245, 255, 250)
AZURE = (204, 255, 255)
BLACK = (0, 0, 0)
BLOCKS = 4
BLOCK_SIDE = 110
MARGIN = 10
WIDTH = BLOCKS * BLOCK_SIDE + MARGIN * (BLOCKS + 1)
HEIGHT = BLOCKS * BLOCK_SIDE + MARGIN * (BLOCKS + 1) + 110
TOP_PANEL = pygame.Rect(0,0,WIDTH,110)
score = 0 #начальная переменная для счета
USERNAME = None      #изначальное имя игрока


l[1][3] = 2
l[2][2] = 4
print(get_empty_list(l))
pretty_print(l)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def draw_intro():         #функция для отображения картинки
    img2048 = pygame.image.load('2048intro.jpg')
    font = pygame.font.SysFont("simsun", 70)
    text_welcome = font.render("Welcome!", True, WHITE_MINT)
    name = 'Введите имя игрока'
    is_find_name = False #переменная, обозначающая, что изначально имя не задано
    while not is_find_name:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:   #если мы нажали на клавиатуру
                    if event.unicode.isalpha():
                        if name == 'Введите имя игрока':
                            name = event.unicode
                        else:
                            name += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(name) > 2:
                            global USERNAME
                        USERNAME = name
                        is_find_name = True
                    break

        screen.fill(BLACK)    #закрашиваем экран черным, чтобы старые значение пропадали и текст не накладывался
        text_name = font.render(name, True, WHITE_MINT) #переменная, зависящая от переменной name
        rect_name = text_name.get_rect()            #переменная для координат текста после приветствия
        rect_name.center = screen.get_rect().center #чтобы текст после приветствия распологался по центру
        screen.blit(pygame.transform.scale(img2048, [200,200]), [10,10]) #прикрепляем заставку на экран
        screen.blit(text_welcome, (230, 65))
        screen.blit(text_name, rect_name)
        #чтобы картинка мэтчилась с размером игры, использую scale из модуля pygame
        pygame.display.update()       #чтобы картинка отобразилась, нужно обновить экран
    screen.fill(BLACK)  #чтобы после нажатия enter, при переходи из intro-окна в основное поле игры, фон обновлялся и был просто чер

def draw_game_over():
    img2048 = pygame.image.load('2048intro.jpg')
    font = pygame.font.SysFont("simsun", 60)
    text_game_over = font.render("Game over!", True, WHITE_MINT)
    text_score = font.render(f"Вы набрали {score}", True, WHITE_MINT)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = 'НОВЫЙ РЕКОРД!'
    else:
        text = f'Рекорд {best_score}'
    text_record = font.render(text, True, WHITE_MINT)
    insert_result(USERNAME, score)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        pygame.display.update()

draw_intro()

draw_interface(score)
pygame.display.update()

#цикл игры
while is_there_an_empty_cell(l) or is_there_a_way_out(l):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0 #до проверки нажатия клавиш счет = 0
            if event.key == pygame.K_LEFT:
                l, delta = move_left(l)
            elif event.key == pygame.K_RIGHT:
                l, delta = move_right(l)
            elif event.key == pygame.K_UP:
                l, delta = move_up(l)
            elif event.key == pygame.K_DOWN:
                l, delta = move_down(l)
            score += delta
            if is_there_an_empty_cell(l):
                empty = get_empty_list(l)
                random.shuffle(empty)
                random_empty_cell = empty.pop()  # удаляем и возвращаем последний элемент уже перемешанного списка(заполненного номерами пустых  ячеек)
                x, y = get_index_from_number(random_empty_cell)
                l = insert_2_or_4(l, x, y)
                print(f'Мы заполнили элемент под номером {random_empty_cell}')
            draw_interface(score, delta)
            pygame.display.update()

    print(USERNAME)   #чтобы убедиться, что имя сохранилось

draw_game_over()
