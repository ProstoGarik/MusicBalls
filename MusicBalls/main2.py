import pygame
WIDTH, HEIGHT = 800, 600

pygame.mixer.init(devicename="HP 27ea (NVIDIA High Definition Audio)")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sound = pygame.mixer.Sound('sound2.mp3')
sound.set_volume(1.0)   # максимум
sound.play()
while pygame.mixer.get_busy():
    pygame.time.delay(100)

pygame.quit()