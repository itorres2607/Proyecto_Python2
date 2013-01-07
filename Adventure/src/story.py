# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys , os
import pygame
from pygame.locals import *



def reproduce_parte(p_ant , keys):
    cont = 0
    if keys == pygame.K_a:
        r = "grabaciones/"+p_ant+"_1.ogg"
        aux = p_ant+"_1"

    elif keys == pygame.K_b:
        r = "grabaciones/"+p_ant+"_2.ogg"
        aux = p_ant+"_2"

    elif keys == pygame.K_c:
        r = "grabaciones/"+p_ant+"_3.ogg"
        aux = p_ant+"_3"

    else:
        r = "ggggg"
        aux = "error"

    #print str(keys)+"------"+str(pygame.K_a)
    #print r
    #pygame.mixer.init()


    try:
        pygame.mixer.music.load(r)
        pygame.mixer.music.play()
    except:
        aux = "error"

    while pygame.mixer.music.get_busy() == True:
        cont = cont+1

    return aux


    
#def reproduce_opcion(o_ant , keys):
#    if keys[K_a] or keys[K_A]:
#        o = "opciones/"+o_ant+"_1.mp3"
#        aux = o_ant+"_1"
#    if keys[K_b] or keys[K_B]:
#        o = "opciones/"+o_ant+"_2.mp3"
#        aux = o_ant+"_2"
#    if keys[K_c] or keys[K_C]:
#        o = "opciones/"+o_ant+"_3.mp3"
#        aux = o_ant+"_3"

#    pygame.mixer.init()
#    try:
#        pygame.mixer.music.load(o)
#        pygame.mixer.music.play()
#    except:
#        aux = "error"


#    return aux



def reproduccion_parte_inicial():
    cont = 0
    pygame.mixer.init()
    pygame.mixer.music.load("grabaciones/parte1.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        cont = cont+1


def reproduccion_mensaje_error():
    cont = 0
    pygame.mixer.init()
    pygame.mixer.music.load("grabaciones/mensaje_error.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        cont = cont+1



#def reproduccion_opcion_inicial():
 #   pygame.mixer.init()
  #  pygame.mixer.music.load("opciones/opcion1.mp3")
   # pygame.mixer.music.play()



def main():
    screen = pygame.display.set_mode((640,480))
    reproduccion_parte_inicial()
    #reproduccion_opcion_inicial()
    parte_anterior = "parte1"
    #opcion_anterior= "opcion1"

    while True:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    sys.exit(0)

                if evento.key == pygame.K_a or evento.key == pygame.K_b or evento.key == pygame.K_c:
                    parte_anterior = reproduce_parte(parte_anterior , evento.key)
                    print parte_anterior
                    #print "------"+str(keys)
                    if parte_anterior == "error":
                        reproduccion_mensaje_error()
                        sys.exit(0)

        pygame.display.flip()


    return 0



if __name__ == "__main__":
    pygame.init()
    main()
