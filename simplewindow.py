#!/usr/bin/env python

import pygame

class Question(pygame.sprite.Sprite):
    def __init__(self):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((140,32))
        text = font.render("7 x 6 = ", 1, (10, 10, 20))
        textpos = text.get_rect()
        textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(gray_red)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((40,500),(40,32))

class Answer(pygame.sprite.Sprite):
    def __init__(self):
        font = pygame.font.Font(None, 36)
        pygame.sprite.Sprite.__init__(self)
        box = pygame.Surface((80,32))
        text = font.render("", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = box.get_rect().centerx
        textpos.centery = box.get_rect().centery
        box.fill(white)
        box.blit(text, textpos)
        self.image = box
        self.rect = ((185,500),(40,32))



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
    while running:
        for event in pygame.event.get():
	    if (event.type == pygame.QUIT or 
	        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
	        running = False
        for b in boxes:
            window.blit(b.image,b.rect)
        question = Question() # generate a question
        window.blit(question.image, question.rect)
        answer = Answer() 
        window.blit(answer.image, answer.rect)
    
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


