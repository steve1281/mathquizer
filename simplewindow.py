#!/usr/bin/env python
import pygame

from quiz import quiz
 
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


if  __name__ == "__main__":
    pygame.init()

    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    gray_red = pygame.Color(200, 100, 100)
    black = pygame.Color(0, 0, 0)
    gray = pygame.Color(100, 100, 100)
    yellow = pygame.Color(255, 255, 100)


    size = width, height = 800, 640
    font = pygame.font.Font(None, 36)
    window = pygame.display.set_mode(size)
    window.fill(gray)
    boxes = [] #pygame.sprite.Group() 

    for i in range(1, 13):
        for j in range(1, 13):
            box = pygame.Surface((40,32))
            sbox = pygame.sprite.Sprite()
            text = font.render(str(i*j), 1, (10, 10, 20))
            textpos = text.get_rect()
            textpos.centerx = box.get_rect().centerx
            textpos.centery = box.get_rect().centery
            box.fill(gray_red)
            box.blit(text, textpos)
            sbox.image = box
            sbox.rect = ((i*46,j*38),(40,32)) 
            boxes.append(sbox)

    running = True
    entered = ""
    question_number = 0
    feedback = None
 
    actual_answer = quiz[question_number]['answer']
    question_text = quiz[question_number]['question']
    while running:
        window.fill(gray)
        for event in pygame.event.get():
	    if (event.type == pygame.QUIT or 
	        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
	        running = False
            if event.type == pygame.KEYDOWN:
                feedback = None
                if event.key == pygame.K_0:
                    entered = entered + "0"
                elif event.key == pygame.K_1:
                    entered = entered + "1"
                elif event.key == pygame.K_2:
                    entered = entered + "2"
                elif event.key == pygame.K_3:
                    entered = entered + "3"
                elif event.key == pygame.K_4:
                    entered = entered + "4"
                elif event.key == pygame.K_5:
                    entered = entered + "5"
                elif event.key == pygame.K_6:
                    entered = entered + "6"
                elif event.key == pygame.K_7:
                    entered = entered + "7"
                elif event.key == pygame.K_8:
                    entered = entered + "8"
                elif event.key == pygame.K_9:
                    entered = entered + "9"
                elif event.key == pygame.K_BACKSPACE:
                    entered = entered[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(entered) > 0:
                        ans = int(entered)
                    else:
                        ans = -1  # always wrong
                    if ans == actual_answer:
                        question_number += 1
                        if question_number == len(quiz):
                            question_number = 0
                        actual_answer = quiz[question_number]['answer'] 
                        question_text = quiz[question_number]['question']
                        entered = ""
                        feedback = Feedback("Got last question, try another!")
                    else:
                        feedback = Feedback("Last try was wrong, try again.")
                        # display pass button
                   


        for b in boxes:
            window.blit(b.image,b.rect)
        question = Question(question_text) 
        window.blit(question.image, question.rect)
        answer = Answer(entered) 
        window.blit(answer.image, answer.rect)
        if feedback:
            window.blit(feedback.image, feedback.rect)
   
    
        pygame.display.update()
        pos = pygame.mouse.get_pos()
        for i in range(len(boxes)):
            s = boxes[i]
            r = pygame.Rect( s.rect)
            if r.collidepoint(pos[0],pos[1]):
                pygame.draw.rect(s.image, yellow, pygame.Rect((0,0),(44,32)),3)
                s1 = boxes[i % 12]
                s2 = boxes[i - i% 12]
                pygame.draw.rect(s1.image, yellow, pygame.Rect((0,0),(44,32)),3)
                pygame.draw.rect(s2.image, yellow, pygame.Rect((0,0),(44,32)),3)
            else:
                pygame.draw.rect(s.image, gray_red, pygame.Rect((0,0),(44,32)),3)

 
    pygame.quit()


