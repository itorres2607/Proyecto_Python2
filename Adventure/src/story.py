# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys , os
import pygame
from pygame.locals import *


# funcion encargada de determinar que parte de la hisoria el usuario decidio continuar
def reproduce_parte(p_ant , keys):
    cont = 0
    if keys == pygame.K_a: #si aplasto la tecla a
        r = "grabaciones/"+p_ant+"_1.ogg" #variable a reproducir
        aux = p_ant+"_1" # variable que guarda la parte actual en reproduccion

    elif keys == pygame.K_b: # si aplasto la tecla b
        r = "grabaciones/"+p_ant+"_2.ogg"
        aux = p_ant+"_2"

    else:
        r = "ggggg"
        aux = "error"

    


    try:
        pygame.mixer.music.load(r)
        pygame.mixer.music.play()
    except:
        aux = "error"

    while pygame.mixer.music.get_busy() == True:
        cont = cont+1

    return aux


    




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







def main(): 
    screen = pygame.display.set_mode((640,480))
    # se ejecuta una pantalla para mantener el foco del programa, ya que facilmente el usuario puede dar clic sin querer en otro lado y no se capturan los eventos de teclado
    reproduccion_parte_inicial()
    
    parte_anterior = "parte1"
    #al inicio la parte anterior es la primera

    while True:
        eventos = pygame.event.get()
        #obtengo todos los eventos que el usuario realice
        for evento in eventos:
            if evento.type == pygame.KEYDOWN: #si el usuario aplasto una tecla
                if evento.key == pygame.K_q or evento.key == K_ESCAPE: # si fue la q o escape
                    sys.exit(0)

                if evento.key == pygame.K_a or evento.key == pygame.K_b:   
                    parte_anterior = reproduce_parte(parte_anterior , evento.key)
                    # reproduzco y recupero la parte que se esta reproduciendo
                    if parte_anterior == "error":
                    # si hubo algun error al reproducir la opcion escogida por el usuario
                        reproduccion_mensaje_error()
                        sys.exit(0)

        pygame.display.flip() #muestra la pantalla todas las veces


    return 0 # fin del programa



if __name__ == "__main__":
    pygame.init() #inicializa pygame
    main()
