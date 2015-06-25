#!/usr/bin/env python
import time
from math import ceil
import pygame
from quiz import quiz
from sprites import Chicken, Question, Answer, Feedback, TimerBox, ScoreBox
from colors import *


class Main():
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.fps = 30
        size = width, height = 800, 640
        self.window = pygame.display.set_mode(size)
        self.initMathTool()
        self.initSprites()
        self.initGameStats()
        self.runGame()

    def initMathTool(self):
        self.boxes = []  
        for i in range(1, 13):
            for j in range(1, 13):
                box = pygame.Surface((40,32))
                sbox = pygame.sprite.Sprite()
                text = self.font.render(str(i*j), 1, (10, 10, 20))
                textpos = text.get_rect()
                textpos.centerx = box.get_rect().centerx
                textpos.centery = box.get_rect().centery
                box.fill(gray_red)
                box.blit(text, textpos)
                sbox.image = box
                sbox.rect = ((i*46,j*38),(40,32)) 
                self.boxes.append(sbox)

    def initSprites(self):
        self.chickens = [ Chicken(600, 10), Chicken(660, 5), Chicken(720, 10)]
        self.timerbox = TimerBox("0")
        self.question = Question("")
        self.scorebox = ScoreBox("")
        self.answer = Answer("")
        self.feedback = Feedback("")

    def initGameStats(self):
        self.chicken_count = len(self.chickens)
        self.timer_set = 30  
        self.entered = ""
        self.question_number = 0
        self.question_count = 10
        self.old_time = 0
        self.start_time = time.time()
        self.actual_answer = quiz[self.question_number]['answer']
        self.question_text = quiz[self.question_number]['question']
    
    def decode(self, key):
        k = key - pygame.K_0
        if k>=0 and k <= 9:
            return str(k)
        else:
            return ""

    def runGame(self):
        running_game = True
        running_intro = False
        running_done = False    
        running = True

        while running:
            self.window.fill(gray)
            if running_game:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or 
                        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                    if event.type == pygame.KEYDOWN:
                        self.feedback.setText("")
                        self.entered = self.entered + self.decode(event.key)
                        if event.key == pygame.K_BACKSPACE:
                            self.entered = self.entered[:-1]
                        elif event.key == pygame.K_RETURN:
                            if len(self.entered) > 0:
                                ans = int(self.entered)
                            else:
                                ans = -1  
                            if ans == self.actual_answer:
                                self.question_number += 1
                                if self.question_number == len(quiz):
                                    self.question_number = 0
                                if self.question_number == self.question_count: 
                                    endtime = time.time()
                                self.actual_answer = quiz[self.question_number]['answer'] 
                                self.question_text = quiz[self.question_number]['question']
                                self.entered = ""
                                self.feedback.setText("Got last question, try another!")
                            else:
                                self.feedback.setText("Last try was wrong, try again.")
                                self.chicken_count -= 1
                                if self.chicken_count < 0:
                                    self.chicken_count = 0
                                # display pass button

                for b in self.boxes:
                    self.window.blit(b.image,b.rect)

                self.question.setText(self.question_text) 
                self.window.blit(self.question.image, self.question.rect)
                self.answer.setText(self.entered) 
                self.window.blit(self.answer.image, self.answer.rect)
                self.window.blit(self.feedback.image, self.feedback.rect)
                score = self.timer_set - (time.time() - self.start_time )
                score = int(ceil(score))
                if self.old_time <> score:
                    self.old_time = score
                    self.timerbox.setText(str(score))
                if self.timerbox:
                    self.window.blit(self.timerbox.image, self.timerbox.rect)

                if score <= 0:
                    running_game = False
                    running_done = True

                self.scorebox.setText(str(self.question_number))
                self.window.blit(self.scorebox.image, self.scorebox.rect)

                for i in range(self.chicken_count):
                    self.window.blit(self.chickens[i].image, self.chickens[i].rect)
   
                pos = pygame.mouse.get_pos()
                for i in range(len(self.boxes)):
                    s = self.boxes[i]
                    r = pygame.Rect( s.rect)
                    if r.collidepoint(pos[0],pos[1]):
                        pygame.draw.rect(s.image, yellow, pygame.Rect((0,0),(44,32)),3)
                        s1 = self.boxes[i % 12]
                        s2 = self.boxes[i - i% 12]
                        pygame.draw.rect(s1.image, yellow, pygame.Rect((0,0),(44,32)),3)
                        pygame.draw.rect(s2.image, yellow, pygame.Rect((0,0),(44,32)),3)
                    else:
                        pygame.draw.rect(s.image, gray_red, pygame.Rect((0,0),(44,32)),3)
            elif running_done:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or 
                        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                self.scorebox.setText(str(self.question_number))
                self.window.blit(self.scorebox.image, self.scorebox.rect)
                for i in range(self.chicken_count):
                    self.window.blit(self.chickens[i].image, self.chickens[i].rect)


            self.clock.tick(self.fps) 
            pygame.display.update()

 
        pygame.quit()



if  __name__ == "__main__":
    Main()

