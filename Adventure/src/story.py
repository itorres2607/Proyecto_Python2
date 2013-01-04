# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys , os
import pygame
from pygame.locals import *



def reproduce_parte(p_ant , keys):
    if keys[K_a] or keys[K_A]:
        r = "grabaciones/"+p_ant+"_1.mp3"
        aux = p_ant+"_1"

    if keys[K_b] or keys[K_B]:
        r = "grabaciones/"+p_ant+"_2.mp3"
        aux = p_ant+"_2"
        
    if keys[K_c] or keys[K_C]:
        r = "grabaciones/"+p_ant+"_3.mp3"
        aux = p_ant+"_3"

    pygame.mixer.init()


    try:
        pygame.mixer.music.load(r)
        pygame.mixer.music.play()
    except:
        aux = "error"


    return aux


    
def reproduce_opcion(o_ant , keys):
    if keys[K_a] or keys[K_A]:
        o = "opciones/"+o_ant+"_1.mp3"
        aux = o_ant+"_1"
    if keys[K_b] or keys[K_B]:
        o = "opciones/"+o_ant+"_2.mp3"
        aux = o_ant+"_2"
    if keys[K_c] or keys[K_C]:
        o = "opciones/"+o_ant+"_3.mp3"
        aux = o_ant+"_3"

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(o)
        pygame.mixer.music.play()
    except:
        aux = "error"


    return aux



def reproduccion_parte_inicial():
    pygame.mixer.init()
    pygame.mixer.music.load("grabaciones/parte1.mp3")
    pygame.mixer.music.play()



def reproduccion_opcion_inicial():
    pygame.mixer.init()
    pygame.mixer.music.load("opciones/opcion1.mp3")
    pygame.mixer.music.play()



def main():

    reproduccion_parte_inicial()
    reproduccion_opcion_inicial()
    parte_anterior = "parte1"
    opcion_anterior= "opcion1"


    while True:
        keys = pygame.key.get_pressed()
        opcion_anterior = reproduce_opcion(opcion_anterior , keys)
        parte_anterior = reproduce_parte(parte_anterior , keys)

        if parte_anterior == "error" or opcion_anterior == "error":
            sys.exit(0)

    return 0



if __name__ == "__main__":
    pygame.init()
    main()
