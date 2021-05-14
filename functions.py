import random

def pretty_print(l):#функция, которая принимает массив и проходя по всем рядам массива, печатает каждый вложенный список
    print('-'*10) #чтобы отделять один вывод от другого
    for row in l:
        print(*row)
    print('-' * 10)

def get_number_from_index(i, j): #функция, которая принимает номер строки и номер столбцами возвращает порядковый номер элемента
    return i * 4 + j + 1

def get_index_from_number(num):  #функция, которая по числу выдает координаты ячейки
    num -= 1
    x,y = num // 4, num % 4
    return x,y

def insert_2_or_4(l,x,y):        #функция, вставляющая двойку или четверку в массив
    if random.random()<=0.8:    #так как в оригинальной игре двойка выпадает чаще, чем четверка, увеличим вероятность выпадения двойки с 50% до 80%
        l[x][y] = 2
    else:
        l[x][y] = 4
    return l

def get_empty_list(l): #функция для нахождения пустых мест в списке
    empty = [] #список, в который записываются все порядковые номера пустых ячеек
    for i in range(4):
        for j in range(4):
            if l[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty

def is_there_an_empty_cell(l):
    for row in l:
        if 0 in row:
            return True
    return False

#заставляем ячейки двигаться
def move_left(l):
    for row in l:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if l[i][j] == l[i][j + 1] and l[i][j] != 0:
                l[i][j] *= 2
                l[i].pop(j + 1)
                l[i].append(0)
    return l

def move_right(l):
    for row in l:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0) #вставляем нули вначало, потому что ответ должен складываться направо
    for i in range(4):
        for j in range(3, 0, -1):
            if l[i][j] == l[i][j - 1] and l[i][j] != 0:
                l[i][j] *= 2
                l[i].pop(j - 1)
                l[i].insert(0, 0)
    return l

def move_up(l):
    for j in range(4):
        column = []
        for i in range(4):
            if l[i][j] != 0:
                column.append(l[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i + 1] and column[i] != 0:
                column[i] *= 2
                column.pop(i + 1)
                column.append(0)
        for i in range(4):
            l[i][j] = column[i]
    return l

def move_down(l):
    for j in range(4):
        column = []
        for i in range(4):
            if l[i][j] != 0:
                column.append(l[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:
                column[i] *= 2
                column.pop(i - 1)
                column.insert(0, 0)
        for i in range(4):
            l[i][j] = column[i]
    return l

def is_there_a_way_out(l):
    for i in range(3):
        for j in range(3):
            if l[i][j] == l[i][j + 1] or l[i][j] == l[i + 1][j]:
                return True
    return False



