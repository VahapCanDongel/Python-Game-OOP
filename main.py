import pygame
pygame.init()

screen = pygame.display.set_mode([1000, 500])

        
class Charactor:
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
        

# Alien can be inherited from player. 
class Alien(Charactor):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    
class Player(Charactor):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)




alien1 = Alien("assets/alien.png", 100, 100)
player1 = Player("assets/spaceship.png", 700, 250)


class Game:
    def __init__(self, screen_height, screen_width, screen_title):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen_title = screen_title
    
    
    def set_display(self):
        pygame.display.set_mode([self.screen_height, self.screen_width])
    
    def run(self, isGameRunning = True):
        while isGameRunning:

            screen.fill((20, 22, 41))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameRunning = False 
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        alien1.move_right(4)
                        
                        
                        
            screen.blit(alien1.image, (alien1.get_x(), alien1.get_y()))        
            screen.blit(player1.image, (player1.get_x(), player1.get_y()))


            pygame.display.flip()
        
        
        
        
if __name__ == "__main__":
    game = Game(1000, 500, "Game Title")
    game.run()