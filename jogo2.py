import pygame as pg
import random


class PedraPapelTesoura:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)

        self.window = pg.display.set_mode((750, 900))

        pg.font.init()
        self.font_1 = pg.font.SysFont("Courier New", 300, bold=True)
        self.font_2 = pg.font.SysFont("Courier New", 40, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.actions = ['rock', 'paper', 'scissors']
        self.action = None
        self.adversary_action = None

        # Rock
        self.rock_jpg = pg.image.load('./rock.png')
        self.rock_img = pg.transform.scale(self.rock_jpg, (300, 300))
        self.rock_img_action = pg.transform.scale(self.rock_jpg, (100, 100))
        # Paper
        self.paper_jpg = pg.image.load('./paper.png')
        self.paper_img = pg.transform.scale(self.paper_jpg, (300, 300))
        self.paper_img_action = pg.transform.scale(self.paper_jpg, (100, 100))
        # Scissors
        self.scissors_jpg = pg.image.load('./scissors.png')
        self.scissors_img = pg.transform.scale(self.scissors_jpg, (300, 300))
        self.scissors_img_action = pg.transform.scale(self.scissors_jpg, (100, 100))

    def mouse_has_clicked(self, input):
            if self.last_click_status == input:
                return (False, False, False)
            else:
                left_button = False
                center_button = False
                right_button = False
                if self.last_click_status[0] == False and input[0] == True:
                    left_button = True
                if self.last_click_status[1] == False and input[1] == True:
                    center_button = True
                if self.last_click_status[2] == False and input[2] == True:
                    right_button = True

                return (left_button, center_button, right_button)

    def clear_window(self):
        pg.draw.rect(self.window, self.white, (0, 0, self.window.get_width(), self.window.get_height()))

    def board(self):
        pg.draw.circle(self.window, self.black, (375, 200), 150, 5)
        question_text = self.font_1.render('?', 1, self.black)
        blit_x = (self.window.get_width() / 2) - (question_text.get_width() / 2)
        blit_y = 200 - (question_text.get_height() / 2)
        self.window.blit(question_text, (blit_x, blit_y))

        pg.draw.circle(self.window, self.black, (375, 550), 150, 5)
        question_text = self.font_1.render('?', 1, self.black)
        blit_x = (self.window.get_width() / 2) - (question_text.get_width() / 2)
        blit_y = 550 - (question_text.get_height() / 2)
        self.window.blit(question_text, (blit_x, blit_y))

        self.window.blit(self.rock_img_action, (137, 750))
        self.window.blit(self.paper_img_action, (326, 750))
        self.window.blit(self.scissors_img_action, (512, 750))

    