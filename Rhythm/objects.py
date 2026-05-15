import pygame
class Rectangle:
    def __init__(self, x,y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.x = x
        self.y = y
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)