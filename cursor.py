import pygame

class Cursor(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprites\Cursor\cursor.png")
        self.rect = self.image.get_rect()
        self.rect.center=(500, 400)
        self.soundBank = ["Sounds\mouse-click.mp3"]

    def update(self):
        cursor_position = pygame.mouse.get_pos()
        
        self.rect.center = cursor_position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def clickSound(self):
        pygame.mixer.music.load(self.soundBank[0])
        pygame.mixer.music.play()
