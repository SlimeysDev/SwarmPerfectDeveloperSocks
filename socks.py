import pygame

class Socks(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Sprites\Socks\ultrakillsocks.png")
        self.rect = self.image.get_rect()
        self.rect.center=(500, 400)
        self.soundBank = []

    # def update(self):

    def draw(self, surface):
        surface.blit(self.image, self.rect)
