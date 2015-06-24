#!/usr/bin/env python
import pygame
from colors import *

class Chicken(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((50,50))
        box.fill(gray)
        pygame.draw.circle(box, yellow, (25, 25), 20)
        self.rect = ((x, y),(0,0))
        self.image = box


class Question(pygame.sprite.Sprite):
    def __init__(self, question_text):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((140,32))
        text = font.render(question_text + " = ", 1, (10, 10, 20))
        textpos = text.get_rect()
        textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(gray_red)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((40,500),(40,32))

class Answer(pygame.sprite.Sprite):
    def __init__(self, text):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((80,32))
        text = font.render(text+"_", 1, (0, 0, 0))
        textpos = text.get_rect()
        #textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(white)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((185,500),(40,32))

class Feedback(pygame.sprite.Sprite):
    def __init__(self, text):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((400,32))
        text = font.render(text, 1, (0, 0, 0))
        textpos = text.get_rect()
        #textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(white)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((44,550),(400,32))

class TimerBox(pygame.sprite.Sprite):
    def __init__(self, text):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((150,32))
        text = font.render("Timer: "+text, 1, (0, 0, 0))
        textpos = text.get_rect()
        #textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(gray)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((640,150),(150,32))

class ScoreBox(pygame.sprite.Sprite):
    def __init__(self, text):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((150,32))
        text = font.render("Score: "+text, 1, (0, 0, 0))
        textpos = text.get_rect()
        #textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(gray)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((640,250),(150,32))
