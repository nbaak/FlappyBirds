import os
import pygame

bird_images = [] #pygame.transform.scale2x(pygame.image.load(os.path.join("images",f"bird{x}.png"))) for x in range(1,4)]
bird_images.append(pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))))
bird_images.append(pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))))
bird_images.append(pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png"))))

def blitRotateCenter(surf, image, topleft, angle):
    """
    Rotate a surface and blit it to the window
    @param surf: the surface to blit to
    @param image: the image surface to rotate
    @param topLeft: the top left position of the image
    @param angle: a float value for angle
    @return: None
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

class Bird():
    
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 10
    IMAGE_ANIMATION = 5
    IMAGES = bird_images
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.tilt = 0       # rotation
        self.tick_count = 0 # time variable
        self.velocity = 0
        
        self.height = self.y
        
        self.image_count = 0    # for animation
        self.image = self.IMAGES[0] # image to start with
           
    def move_up(self):
        """
        Move the bird upwards
        @return: None
        """
        self.velocity = -10.5   # upwards == negative
        self.tick_count = 0
        self.height = self.y
        
    def move(self):
        """
        Moves the bird downwards
        """
        self.tick_count += 1
        
        # dornwards acceleration
        displacement = self.velocity * self.tick_count + 0.5*3*self.tick_count**2
        
        if displacement >= 16:
            displacement = (displacement/abs(displacement)) * 16
            
        if displacement < 0:
            displacement -= 2
            
        self.y = self.y + displacement  # downwards movement
        
        if displacement < 0 or self.y < self.height +50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
                
            else:
                if self.tilt > -90:
                    self.tilt -= self.ROTATION_VELOCITY
        
    def draw(self, gui):
        """
        Draws the bird on Pygame Gui
        @param gui: Pygame Window
        @return: None
        """
        if self.image_count <= self.IMAGE_ANIMATION:
            self.image = self.IMAGES[0]
        
        elif self.image_count <= self.IMAGE_ANIMATION*2:
            self.image = self.IMAGES[1]
            
        elif self.image_count <= self.IMAGE_ANIMATION*3:
            self.image = self.IMAGES[2]
            
        elif self.image_count <= self.IMAGE_ANIMATION*4:
            self.image = self.IMAGES[1]
            
        elif self.image_count <= self.IMAGE_ANIMATION*4 + 1:
            self.image = self.IMAGES[0]
            self.image_count = 0
            
        else:
            self.image_count = 0
            print ("ERROR: should never reach this point!")
        
        # diving, no flaps
        if self.tilt <= -80:
            self.image = self.IMAGES[1]
            self.image_count = self.IMAGE_ANIMATION*2
            
        blitRotateCenter(gui, self.image, (self.x, self.y), self.tilt)
        
    def get_mask(self):
        """
        get mask of current image
        @return: pixel array
            
        """
        return pygame.mask.from_surface(self.image)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        