import os
import pygame

base_image = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png"))).convert_alpha()

class Base ():
    VELOCITY = 5
    WIDTH = base_image.get_width()
    IMAAGE = base_image
    
    def __init__(self, y):
        self.y = y
        self.x = [0, self.WIDTH]
        
    def move (self):
        '''
        scrolls the base
        @return: None
        '''
        for i in range (len(self.x)):
            self.x[i] -= self.VELOCITY
            
        if self.x[0] + self.WIDTH <= 0:
            self.x.pop(0)
            self.x.append(self.WIDTH)
 
        
    def draw(self, gui):
        """
        @param gui: a pygame windows
        @return: None
        """
        for x in self.x:
            gui.blit(self.IMAAGE, (x, self.y))
        
    