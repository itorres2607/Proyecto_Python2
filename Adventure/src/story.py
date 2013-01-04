# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys , os
import pygame
from pygame.locals import *

def evento_tecla(keys):
    if keys[K_q]:
        sys.exit(0)


def avanza_pagina(pagina):
    pag = "parte"+pagina
    #ejecutar sonido de la parte que corresponde



def retrocede_pagina(pagina):
    pag = "parte"+pagina
    #ejecuto sonido de la parte correspondiente

if __name__ == "__main__":
    print "Hello World"
