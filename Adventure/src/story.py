# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys , os
import pygame
from pygame.locals import *



def reproduce_parte(p_ant , keys):
    if keys[K_a] or keys[K_A]:
        r = p_ant+"_1.mp3"
        aux = p_ant+"_1"

    if keys[K_b] or keys[K_B]:
        r = p_ant+"_2.mp3"
        aux = p_ant+"_2"
        
    if keys[K_c] or keys[K_C]:
        r = p_ant+"_3.mp3"
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
        o = o_ant+"_1.mp3"
        aux = o_ant+"_1"
    if keys[K_b] or keys[K_B]:
        o = o_ant+"_2.mp3"
        aux = o_ant+"_2"
    if keys[K_c] or keys[K_C]:
        o = o_ant+"_3.mp3"
        aux = o_ant+"_3"

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(o)
        pygame.mixer.music.play()
    except:
        aux = "error"


    return aux



def main():

    while True:
        keys = pygame.key.get_pressed()
        parte_anterior = reproduce_parte(parte_anterior , keys)
        opcion_anterior = reproduce_opcion(opcion_anterior , keys)

        if parte_anterior == "error" or opcion_anterior == "error":
            sys.exit(0)

    return 0



if __name__ == "__main__":
    pygame.init()
    main()
