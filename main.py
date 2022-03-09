from tkinter import LEFT
import pygame
pygame.init()

screen = pygame.display.set_mode([1000, 500])

alien = pygame.image.load("assets/alien.png")
alien_x = 700
alien_y = 250


class Player:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
    
    def move_right(self, speed):
        self.x += speed
        
    def move_left(self, speed):
        self.x -= speed
        
    def move_up(self, speed):
        self.y += speed
    
    def move_down(self, speed):
        self.y -= speed
        


class Alien:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        
    def move_right(self, speed):
        self.x += speed
        
    def move_left(self, speed):
        self.x -= speed
        
    def move_up(self, speed):
        self.y += speed
    
    def move_down(self, speed):
        self.y -= speed
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

alien1 = Alien("assets/alien.png", 100, 100)

keys = pygame.key.get_pressed()

gamerunning = True
while gamerunning:

    screen.fill((20, 22, 41))


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False 
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("key pressed")
                alien1.move_right(4)
                
                
                
    screen.blit(alien1.image, (alien1.get_x(), alien1.get_y()))        


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()