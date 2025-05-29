import pygame as pg
import random

pg.mixer.init()
pg.mixer.music.load('musica.ogg')
pg.mixer.music.play(-1)

class PedraPapelTesoura:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.window = pg.display.set_mode((750, 900))
        pg.font.init()
        self.font_1 = pg.font.SysFont("Courier New", 300, bold=True)
        self.font_2 = pg.font.SysFont("Courier New", 40, bold=True)

        self.clock = pg.time.Clock()

        self.last_click_status = (False, False, False)

        self.actions = ['rock', 'paper', 'scissors']
        self.action = None
        self.adversary_action = None

        self.rock_jpg = pg.image.load('./rock.png')
        self.rock_img = pg.transform.scale(self.rock_jpg, (300, 300))
        self.rock_img_action = pg.transform.scale(self.rock_jpg, (100, 100))
        self.paper_jpg = pg.image.load('./paper.png')
        self.paper_img = pg.transform.scale(self.paper_jpg, (300, 300))
        self.paper_img_action = pg.transform.scale(self.paper_jpg, (100, 100))
        self.scissors_jpg = pg.image.load('./scissors.png')
        self.scissors_img = pg.transform.scale(self.scissors_jpg, (300, 300))
        self.scissors_img_action = pg.transform.scale(self.scissors_jpg, (100, 100))

        self.placar_jogador = 0
        self.placar_adversario = 0

        self.pontuou_rodada = False  

    def mouse_has_clicked(self, input):
        if self.last_click_status == input:
            return (False, False, False)
        else:
            left_button = not self.last_click_status[0] and input[0]
            center_button = not self.last_click_status[1] and input[1]
            right_button = not self.last_click_status[2] and input[2]
            return (left_button, center_button, right_button)

    def clear_window(self):
        pg.draw.rect(self.window, self.white, (0, 0, self.window.get_width(), self.window.get_height()))

    def board(self):
        pg.draw.circle(self.window, self.black, (375, 200), 150, 5)
        question_text = self.font_1.render('?', True, self.black)
        blit_x = (self.window.get_width() / 2) - (question_text.get_width() / 2)
        blit_y = 200 - (question_text.get_height() / 2)
        self.window.blit(question_text, (blit_x, blit_y))

        pg.draw.circle(self.window, self.black, (375, 550), 150, 5)
        question_text = self.font_1.render('?', True, self.black)
        blit_x = (self.window.get_width() / 2) - (question_text.get_width() / 2)
        blit_y = 550 - (question_text.get_height() / 2)
        self.window.blit(question_text, (blit_x, blit_y))

        pg.draw.rect(self.window, self.black, (132, 745, 110, 110), 5)
        pg.draw.rect(self.window, self.black, (321, 745, 110, 110), 5)
        pg.draw.rect(self.window, self.black, (507, 745, 110, 110), 5)

        self.window.blit(self.rock_img_action, (137, 750))
        self.window.blit(self.paper_img_action, (326, 750))
        self.window.blit(self.scissors_img_action, (512, 750))

        placar_text = self.font_2.render(f'Jogador: {self.placar_jogador}  |  Adversário: {self.placar_adversario}', True, self.black)
        self.window.blit(placar_text, (15, 10))

    def random_action(self):
        self.adversary_action = random.choice(self.actions)

    def adversary_selected_play(self):
        if self.adversary_action == 'rock':
            self.window.blit(self.rock_img, (225, 50))
        elif self.adversary_action == 'paper':
            self.window.blit(self.paper_img, (225, 50))
        elif self.adversary_action == 'scissors':
            self.window.blit(self.scissors_img, (225, 50))

    def selected_play(self):
        if self.action == 'rock':
            self.window.blit(self.rock_img, (225, 400))
        elif self.action == 'paper':
            self.window.blit(self.paper_img, (225, 400))
        elif self.action == 'scissors':
            self.window.blit(self.scissors_img, (225, 400))

    def actions_buttons(self, mouse):
        x, y = mouse[0]
        click = mouse[2][0]

        if 127 <= x <= 247 and 740 <= y <= 860 and click:
            self.random_action()
            self.action = 'rock'
            self.pontuou_rodada = False
        elif 316 <= x <= 436 and 740 <= y <= 860 and click:
            self.random_action()
            self.action = 'paper'
            self.pontuou_rodada = False
        elif 502 <= x <= 622 and 740 <= y <= 860 and click:
            self.random_action()
            self.action = 'scissors'
            self.pontuou_rodada = False

    def match_result_text(self, is_victory, result):
        if is_victory is not None:
            msg = 'Você ganhou!' if is_victory else 'Você perdeu'
            result_text = self.font_2.render(msg, True, self.black)
            desc_text = self.font_2.render(result, True, self.black)
            x_msg = (self.window.get_width() - result_text.get_width()) / 2
            x_desc = (self.window.get_width() - desc_text.get_width()) / 2
            self.window.blit(result_text, (x_msg, 300))
            self.window.blit(desc_text, (x_desc, 350))
        else:
            emp_text = self.font_2.render('Empate!', True, self.black)
            x_emp = (self.window.get_width() - emp_text.get_width()) / 2
            self.window.blit(emp_text, (x_emp, 320))

    def match_result(self):
        if not self.action or not self.adversary_action:
            return
        
        if self.pontuou_rodada:
            if self.action == self.adversary_action:
                self.match_result_text(None, '')
            else:
                is_win = ((self.action == 'rock' and self.adversary_action == 'scissors') or
                          (self.action == 'paper' and self.adversary_action == 'rock') or
                          (self.action == 'scissors' and self.adversary_action == 'paper'))
                desc = ''
                if (self.action == 'rock' and self.adversary_action == 'scissors') or (self.adversary_action == 'rock' and self.action == 'scissors'):
                    desc = 'Pedra amassa a tesoura'
                elif (self.action == 'paper' and self.adversary_action == 'rock') or (self.adversary_action == 'paper' and self.action == 'rock'):
                    desc = 'Papel cobre a pedra'
                elif (self.action == 'scissors' and self.adversary_action == 'paper') or (self.adversary_action == 'scissors' and self.action == 'paper'):
                    desc = 'Tesoura corta o papel'

                self.match_result_text(is_win, desc)
            return

        if self.action == self.adversary_action:
            self.match_result_text(None, '')
        else:
            is_win = ((self.action == 'rock' and self.adversary_action == 'scissors') or
                      (self.action == 'paper' and self.adversary_action == 'rock') or
                      (self.action == 'scissors' and self.adversary_action == 'paper'))

            if is_win:
                self.placar_jogador += 1
            else:
                self.placar_adversario += 1

            desc = ''
            if (self.action == 'rock' and self.adversary_action == 'scissors') or (self.adversary_action == 'rock' and self.action == 'scissors'):
                desc = 'Pedra amassa a tesoura'
            elif (self.action == 'paper' and self.adversary_action == 'rock') or (self.adversary_action == 'paper' and self.action == 'rock'):
                desc = 'Papel cobre a pedra'
            elif (self.action == 'scissors' and self.adversary_action == 'paper') or (self.adversary_action == 'scissors' and self.action == 'paper'):
                desc = 'Tesoura corta o papel'

            self.match_result_text(is_win, desc)

            self.pontuou_rodada = True

ppt = PedraPapelTesoura()

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
    mouse_click = ppt.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    ppt.clock.tick(60)
    ppt.clear_window()
    ppt.actions_buttons(mouse)
    ppt.board()
    ppt.adversary_selected_play()
    ppt.selected_play()
    ppt.match_result()
    ppt.last_click_status = mouse_input
    pg.display.update()
