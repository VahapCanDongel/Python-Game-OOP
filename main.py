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
        
    def move_down(self, speed):
        self.y += speed
    
    def move_up(self, speed):
        self.y -= speed
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        

class Alien(Charactor):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    
class Player(Charactor):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)


class Game:
    pressed_right = False
    pressed_left = False
    player1 = Player("assets/spaceship.png", 700, 250)
    
    alien_1 = Alien("assets/alien.png", 100, 100)
    alien_2 = Alien("assets/alien.png", 150, 100)
    alien_3 = Alien("assets/alien.png", 200, 100)
    alien_4 = Alien("assets/alien.png", 250, 100)

    aliens = [alien_1, alien_2, alien_3, alien_4]
    
    pressed_right = False
    pressed_left = False
    
    player_speed = 2
    
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
                       self.pressed_right = True
                        
                    if event.key == pygame.K_LEFT:
                        self.pressed_left = True
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.pressed_right = False
                        
                    if event.key == pygame.K_LEFT:
                        self.pressed_left = False
                    
            if self.pressed_right:
                self.player1.move_right(self.player_speed)
            
            if self.pressed_left:
                self.player1.move_left(self.player_speed)    
            
            for alien in self.aliens:
                screen.blit(alien.image, (alien.get_x(), alien.get_y()))
            
            for x in self.aliens:
                    if x.get_x() < 500:
                        x.move_down(0.006)
                        
                            
            screen.blit(self.player1.image, (self.player1.get_x(), self.player1.get_y()))
            
            pygame.display.flip()
        
if __name__ == "__main__":
    game = Game(1000, 500, "Game Title")
    game.run()