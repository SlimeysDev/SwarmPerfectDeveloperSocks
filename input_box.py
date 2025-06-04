import pygame

class input_box():

    def __init__(self, width, height, text):
        super().__init__()
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect((0,0), (width, height))
        self.rect.center = (500, 400)
        self.font = pygame.font.Font(None, 32)
        self.color_inactive = pygame.Color((255, 255, 255))
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False