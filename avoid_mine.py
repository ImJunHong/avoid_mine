import pygame as pg
import random
import sys

background_color = (50, 50, 50)
black = (0, 0, 0)
white = (255, 255, 255)
dark_white = (235, 235, 235)
cyan = (100, 180, 255)
green = (51, 204, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

margin = 100
cell_size = 40
cell_num = 15
screen_size = [margin*2 + cell_size*cell_num, margin*2 + cell_size*cell_num]
coordinate = [[0 for y in range(cell_num)] for x in range(cell_num)]
current_coordinate = [0, 0]
secured_coordinate = [(0, 0)]
initial_cells = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
show_list = []

def main():
    pg.init()
    screen = pg.display.set_mode(screen_size)
    font = pg.font.SysFont("Times New Roman", margin*3//10)
    pg.display.set_caption("지뢰피하기")
    fps = 60

    rects = draw_menu(font, screen)
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                select_level(event.pos, rects, screen, font, fps)
            elif event.type == pg.QUIT:
                exit()

def select_level(pos, rects, screen, font, fps):
    if rects[0].collidepoint(pos):
        level = "easy"
        start_game(screen, font, fps, level)

def start_game(screen, font, fps, level):
    set_path() # 시작점에서 도착점으로 가는 최단경로 설정
    set_mines(level) # 지뢰 생성 및 지뢰 알림 숫자 설정
    
    clock = pg.time.Clock()
    fail = False

    while not fail:
        clock.tick(fps)
        screen.fill(background_color)
        draw_secured_cells(screen)
        draw_board(screen)
        show_numbers(font, screen)
        draw_me(screen)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                pressed = pg.key.get_pressed()
                keynames = [pg.key.name(key) for key, value in enumerate(pressed) if value]

                for key in keynames:
                    if key == "up" and current_coordinate[1] > 0:
                        current_coordinate[1] -= 1
                        secure_cell(font, screen)
                    elif key == "down" and current_coordinate[1] < cell_num-1:
                        current_coordinate[1] += 1
                        secure_cell(font, screen)
                    elif key == "left" and current_coordinate[0] > 0:
                        current_coordinate[0] -= 1
                        secure_cell(font, screen)
                    elif key == "right" and current_coordinate[0] < cell_num-1:
                        current_coordinate[0] += 1
                        secure_cell(font, screen)

            elif event.type == pg.QUIT:
                exit()
        
        pg.display.flip()

def print_text(font, screen, msg, color, pos):
    textSurface = font.render(msg, True, color, None)
    textRect = textSurface.get_rect()
    textRect.center = pos
    screen.blit(textSurface, textRect)
    return textRect

def set_path():
    x, y = 0, 0
    while x+y < (cell_num-1)*2:
        if random.random() > 0.5 and x < cell_num-1:
            x += 1
            coordinate[y][x] = "P"
        elif y < cell_num-1:
            y += 1
            coordinate[y][x] = "P"

def set_mines(level):
    if level == "easy":
        mine_num = (cell_num**2)//4

    minefield = list(range(1, cell_num**2))
    for y in range(cell_num):
        for x in range(cell_num):
            if coordinate[y][x] == "P":
                minefield.remove(y*cell_num + x)
                coordinate[y][x] = 0
    mine_list = random.sample(minefield, mine_num)
    for mine in mine_list:
        mine_X = mine%cell_num
        mine_Y = mine//cell_num
        coordinate[mine_Y][mine_X] = "M"
        
        if mine_Y > 0 and coordinate[mine_Y - 1][mine_X] != "M": # 상
            coordinate[mine_Y - 1][mine_X] += 1
        if mine_Y < cell_num-1 and coordinate[mine_Y + 1][mine_X] != "M": # 하
            coordinate[mine_Y + 1][mine_X] += 1
        if mine_X > 0 and coordinate[mine_Y][mine_X - 1] != "M": # 좌
            coordinate[mine_Y][mine_X - 1] += 1
        if mine_X < cell_num-1 and coordinate[mine_Y][mine_X + 1] != "M": # 우
            coordinate[mine_Y][mine_X + 1] += 1
        if mine_Y > 0 and mine_X > 0 and coordinate[mine_Y - 1][mine_X - 1] != "M": # 좌상
            coordinate[mine_Y - 1][mine_X - 1] += 1
        if mine_Y < cell_num-1 and mine_X > 0 and coordinate[mine_Y + 1][mine_X - 1] != "M": # 좌하
            coordinate[mine_Y + 1][mine_X - 1] += 1
        if mine_Y > 0 and mine_X < cell_num-1 and coordinate[mine_Y - 1][mine_X + 1] != "M": # 우상
            coordinate[mine_Y - 1][mine_X + 1] += 1
        if mine_Y < cell_num-1 and mine_X < cell_num-1 and coordinate[mine_Y + 1][mine_X + 1] != "M": # 우하
            coordinate[mine_Y + 1][mine_X + 1] += 1

    for i in coordinate: print(i)

def draw_secured_cells(screen):
    for x, y in secured_coordinate:
        pg.draw.rect(screen, dark_white, [margin + cell_size*x, margin + cell_size*y, cell_size, cell_size])
    pg.draw.rect(screen, yellow, [margin + cell_size*(cell_num-1), margin + cell_size*(cell_num-1), cell_size, cell_size])

def draw_board(screen):
    for i in range(cell_num+1):
        pg.draw.aaline(screen, white, [margin, margin + cell_size*i], [margin + cell_size*cell_num, margin + cell_size*i])
        pg.draw.aaline(screen, white, [margin + cell_size*i, margin], [margin + cell_size*i, margin + cell_size*cell_num])

def show_numbers(font, screen):
    for x, y in secured_coordinate:
        if y > 0 and (x, y-1) not in show_list: # 상
            show_list.append((x, y-1))
        if y < cell_num-1 and (x, y+1) not in show_list: # 하
            show_list.append((x, y+1))
        if x > 0 and (x-1, y) not in show_list: # 좌
            show_list.append((x-1, y))
        if x < cell_num-1 and (x+1, y) not in show_list: # 우
            show_list.append((x+1, y))
        if x > 0 and y > 0 and (x-1, y-1) not in show_list: # 좌상
            show_list.append((x-1, y-1))
        if x > 0 and y < cell_num-1 and (x-1, y+1) not in show_list: # 좌하
            show_list.append((x-1, y+1))
        if x < cell_num-1 and y > 0 and (x+1, y-1) not in show_list: # 우상
            show_list.append((x+1, y-1))
        if x < cell_num-1 and y < cell_num-1 and (x+1, y+1) not in show_list: # 우하
            show_list.append((x+1, y+1))

    for x, y in show_list:
        value = coordinate[y][x]
        text = str(value)
        if value != "M" and value != cell_num**2-1:
            if value < 3:
                print_text(font, screen, text, blue,\
                            (margin + cell_size//2 + cell_size*x, margin + cell_size//2 + cell_size*y))
            elif value < 5:
                print_text(font, screen, text, green,\
                            (margin + cell_size//2 + cell_size*x, margin + cell_size//2 + cell_size*y))
            else:
                print_text(font, screen, text, red,\
                            (margin + cell_size//2 + cell_size*x, margin + cell_size//2 + cell_size*y))

    for x, y in initial_cells:
        if coordinate[y][x] == "M":
            bomb_img = pg.image.load("bomb.png")
            bomb = pg.transform.scale(bomb_img, (cell_size, cell_size))
            screen.blit(bomb, (margin + cell_size*x, margin + cell_size*y))

def draw_me(screen):
    pg.draw.rect(screen, cyan, [margin + cell_size//8 + cell_size*current_coordinate[0],\
                                margin + cell_size//8 + cell_size*current_coordinate[1],\
                                (cell_size*3)//4, (cell_size*3)//4])

def draw_menu(font, screen):
    easy_rect = print_text(font, screen, "Easy", green, (margin + cell_size , (margin*3)//2 + cell_size*cell_num))
    return [easy_rect]

def secure_cell(font, screen):
    if (current_coordinate[0], current_coordinate[1]) not in secured_coordinate:
        secured_coordinate.append((current_coordinate[0], current_coordinate[1]))

    draw_secured_cells(screen)
    draw_board(screen)
    show_numbers(font, screen)
    draw_me(screen)

def exit():
    pg.quit()
    sys.exit()

main()
