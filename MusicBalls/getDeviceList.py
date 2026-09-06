import pygame
import pygame._sdl2.audio as sdl2_audio

pygame.init()
devices = sdl2_audio.get_audio_device_names(False)
for i in devices:
    print(i)