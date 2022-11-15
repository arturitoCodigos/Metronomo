import os
import sounds
import time

class Metronomo:

    def __init__(self, bpm=60, volume=1, sound_type=1):
        self.__bpm = bpm/60 # As funcoes internas necessitam da conversao para Hz
        self.__volume = volume
        self.__on = True

        # Gerando o som
        self.__sound_name = os.path.join("sound_files", str(sound_type) + ".wav")

        # Carregando sua versao pygame
        self.__sound_data = sounds.gen_pygame_sound(self.__sound_name, self.__volume)

    # Getters & Setters
    def getBpm(self):
        return self.__bpm
    
    def setBpm(self, bpm):
        self.__bpm = bpm
    
    def getVolume(self):
        return self.__volume
    
    def setVolume(self, volume):
        self.__volume = volume

    def getOn(self):
        return self.__on
    
    def setOn(self, on):
        self.__on = on
    
    # Methods
    def reload(self):
        self.__sound_data = sounds.gen_pygame_sound(self.__sound_name, self.__volume)

    def beep(self):
        t = 1/self.__bpm
        while self.__on:
            self.__sound_data.play()
            time.sleep(t)