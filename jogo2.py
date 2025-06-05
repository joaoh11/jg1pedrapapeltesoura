import pygame as pg
import random
pg.mixer.init()
pg.mixer.music.load('musica.ogg')
pg.mixer.music.play(-1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW = pg.display.set_mode((750, 900))
pg.font.init()
FONT_1 = pg.font.SysFont("Courier New", 300, bold=True)
FONT_2 = pg.font.SysFont("Courier New", 40, bold=True)

CLOCK = pg.time.Clock()

LAST_CLICK_STATUS = (False, False, False)

ACTIONS = ['rock', 'paper', 'scissors']
ACTION = None
ADVERSARY_ACTION = None

ROCK_JPG = pg.image.load('./rock.png')
ROCK_IMG = pg.transform.scale(ROCK_JPG, (300, 300))
ROCK_IMG_ACTION = pg.transform.scale(ROCK_JPG, (100, 100))
PAPER_JPG = pg.image.load('./paper.png')
PAPER_IMG = pg.transform.scale(PAPER_JPG, (300, 300))
PAPER_IMG_ACTION = pg.transform.scale(PAPER_JPG, (100, 100))
SCISSORS_JPG = pg.image.load('./scissors.png')
SCISSORS_IMG = pg.transform.scale(SCISSORS_JPG, (300, 300))
SCISSORS_IMG_ACTION = pg.transform.scale(SCISSORS_JPG, (100, 100))

PLACAR_JOGADOR = 0
PLACAR_ADVERSARIO = 0

PONTUOU_RODADA = False

def mouse_has_clicked(input_status):
    global LAST_CLICK_STATUS
    if LAST_CLICK_STATUS == input_status:
        return (False, False, False)
    else:
        left_button = not LAST_CLICK_STATUS[0] and input_status[0]
        center_button = not LAST_CLICK_STATUS[1] and input_status[1]
        right_button = not LAST_CLICK_STATUS[2] and input_status[2]
        return (left_button, center_button, right_button)

def clear_window():
    global WINDOW, WHITE
    pg.draw.rect(WINDOW, WHITE, (0, 0, WINDOW.get_width(), WINDOW.get_height()))

def board():
    global WINDOW, BLACK, FONT_1, FONT_2, ROCK_IMG_ACTION, PAPER_IMG_ACTION, SCISSORS_IMG_ACTION, PLACAR_JOGADOR, PLACAR_ADVERSARIO
    pg.draw.circle(WINDOW, BLACK, (375, 200), 150, 5)
    question_text = FONT_1.render('?', True, BLACK)
    blit_x = (WINDOW.get_width() / 2) - (question_text.get_width() / 2)
    blit_y = 200 - (question_text.get_height() / 2)
    WINDOW.blit(question_text, (blit_x, blit_y))

    pg.draw.circle(WINDOW, BLACK, (375, 550), 150, 5)
    question_text = FONT_1.render('?', True, BLACK)
    blit_x = (WINDOW.get_width() / 2) - (question_text.get_width() / 2)
    blit_y = 550 - (question_text.get_height() / 2)
    WINDOW.blit(question_text, (blit_x, blit_y))

    pg.draw.rect(WINDOW, BLACK, (132, 745, 110, 110), 5)
    pg.draw.rect(WINDOW, BLACK, (321, 745, 110, 110), 5)
    pg.draw.rect(WINDOW, BLACK, (507, 745, 110, 110), 5)

    WINDOW.blit(ROCK_IMG_ACTION, (137, 750))
    WINDOW.blit(PAPER_IMG_ACTION, (326, 750))
    WINDOW.blit(SCISSORS_IMG_ACTION, (512, 750))

    placar_text = FONT_2.render(f'Jogador: {PLACAR_JOGADOR}  |  Adversário: {PLACAR_ADVERSARIO}', True, BLACK)
    WINDOW.blit(placar_text, (15, 10))

def random_action():
    global ADVERSARY_ACTION, ACTIONS
    ADVERSARY_ACTION = random.choice(ACTIONS)

def adversary_selected_play():
    global ADVERSARY_ACTION, WINDOW, ROCK_IMG, PAPER_IMG, SCISSORS_IMG
    if ADVERSARY_ACTION == 'rock':
        WINDOW.blit(ROCK_IMG, (225, 50))
    elif ADVERSARY_ACTION == 'paper':
        WINDOW.blit(PAPER_IMG, (225, 50))
    elif ADVERSARY_ACTION == 'scissors':
        WINDOW.blit(SCISSORS_IMG, (225, 50))

def selected_play():
    global ACTION, WINDOW, ROCK_IMG, PAPER_IMG, SCISSORS_IMG
    if ACTION == 'rock':
        WINDOW.blit(ROCK_IMG, (225, 400))
    elif ACTION == 'paper':
        WINDOW.blit(PAPER_IMG, (225, 400))
    elif ACTION == 'scissors':
        WINDOW.blit(SCISSORS_IMG, (225, 400))

def actions_buttons(mouse):
    global ACTION, PONTUOU_RODADA
    x, y = mouse[0]
    click = mouse[2][0]

    if 127 <= x <= 247 and 740 <= y <= 860 and click:
        random_action()
        ACTION = 'rock'
        PONTUOU_RODADA = False
    elif 316 <= x <= 436 and 740 <= y <= 860 and click:
        random_action()
        ACTION = 'paper'
        PONTUOU_RODADA = False
    elif 502 <= x <= 622 and 740 <= y <= 860 and click:
        random_action()
        ACTION = 'scissors'
        PONTUOU_RODADA = False

def match_result_text(is_victory, result):
    global WINDOW, BLACK, FONT_2
    if is_victory is not None:
        msg = 'Você ganhou!' if is_victory else 'Você perdeu'
        result_text = FONT_2.render(msg, True, BLACK)
        desc_text = FONT_2.render(result, True, BLACK)
        x_msg = (WINDOW.get_width() / 2) - (result_text.get_width() / 2)
        x_desc = (WINDOW.get_width() / 2) - (desc_text.get_width() / 2)
        WINDOW.blit(result_text, (x_msg, 300))
        WINDOW.blit(desc_text, (x_desc, 350))
    else:
        emp_text = FONT_2.render('Empate!', True, BLACK)
        x_emp = (WINDOW.get_width() / 2) - (emp_text.get_width() / 2)
        WINDOW.blit(emp_text, (x_emp, 320))

def match_result():
    global ACTION, ADVERSARY_ACTION, PLACAR_JOGADOR, PLACAR_ADVERSARIO, PONTUOU_RODADA
    if not ACTION or not ADVERSARY_ACTION:
        return
    
    if PONTUOU_RODADA:
        if ACTION == ADVERSARY_ACTION:
            match_result_text(None, '')
        else:
            is_win = ((ACTION == 'rock' and ADVERSARY_ACTION == 'scissors') or
                      (ACTION == 'paper' and ADVERSARY_ACTION == 'rock') or
                      (ACTION == 'scissors' and ADVERSARY_ACTION == 'paper'))
            desc = ''
            if (ACTION == 'rock' and ADVERSARY_ACTION == 'scissors') or (ADVERSARY_ACTION == 'rock' and ACTION == 'scissors'):
                desc = 'Pedra amassa a tesoura'
            elif (ACTION == 'paper' and ADVERSARY_ACTION == 'rock') or (ADVERSARY_ACTION == 'paper' and ACTION == 'rock'):
                desc = 'Papel cobre a pedra'
            elif (ACTION == 'scissors' and ADVERSARY_ACTION == 'paper') or (ADVERSARY_ACTION == 'scissors' and ACTION == 'paper'):
                desc = 'Tesoura corta o papel'

            match_result_text(is_win, desc)
        return

    if ACTION == ADVERSARY_ACTION:
        match_result_text(None, '')
    else:
        is_win = ((ACTION == 'rock' and ADVERSARY_ACTION == 'scissors') or
                  (ACTION == 'paper' and ADVERSARY_ACTION == 'rock') or
                  (ACTION == 'scissors' and ADVERSARY_ACTION == 'paper'))

        if is_win:
            PLACAR_JOGADOR += 1
        else:
            PLACAR_ADVERSARIO += 1

        desc = ''
        if (ACTION == 'rock' and ADVERSARY_ACTION == 'scissors') or (ADVERSARY_ACTION == 'rock' and ACTION == 'scissors'):
            desc = 'Pedra amassa a tesoura'
        elif (ACTION == 'paper' and ADVERSARY_ACTION == 'rock') or (ADVERSARY_ACTION == 'paper' and ACTION == 'rock'):
            desc = 'Papel cobre a pedra'
        elif (ACTION == 'scissors' and ADVERSARY_ACTION == 'paper') or (ADVERSARY_ACTION == 'scissors' and ACTION == 'paper'):
            desc = 'Tesoura corta o papel'

        match_result_text(is_win, desc)

        PONTUOU_RODADA = True

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    mouse_position = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    CLOCK.tick(60)
    clear_window()
    actions_buttons(mouse)
    board()
    adversary_selected_play()
    selected_play()
    match_result()
    LAST_CLICK_STATUS = mouse_input
    pg.display.update()