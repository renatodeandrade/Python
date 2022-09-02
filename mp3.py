import pygame
pygame.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('alarme.ogg')
pygame.mixer.music.play()
pygame.event.wait()