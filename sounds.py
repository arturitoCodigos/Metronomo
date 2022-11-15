import pygame as pg

pg.mixer.init()

def gen_pygame_sound(sound_name, volume):
    sound = pg.mixer.Sound(sound_name)
    sound.set_volume(volume)
    return sound
    