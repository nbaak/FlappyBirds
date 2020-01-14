import os
import random
import pygame


pipe_image = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png"))).convert_alpha()



class Pipe():
    
    GAP = 200
    VELOCITY = 5
    
    def __init__(self, x):
        
        self.x = x
        self.height = 0
        
        self.top = 0
        self.bottom = 0
        
        self.PIPE_TOP = pygame.transform.flip(pipe_image, False, True)
        self.PIPE_BOTTOM = pipe_image
        
        self.passed = False
        
        self.set_height()
        
    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP
        
    def move(self):
        self.x -= self.VELOCITY
        
    def draw(self, gui):
        """
        draws the pipe
        @param gui: a pygame windows
        @return: None
        """
        gui.blit(self.PIPE_TOP, (self.x, self.top))
        gui.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        """
        check if pipe and bird are colliding
        @param bird: a Bird Object
        @return: None
        """
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)
        
        if b_point or t_point:
            return True
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        