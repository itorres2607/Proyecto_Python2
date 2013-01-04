# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys , os
import pygame
from pygame.locals import *

def evento_tecla(keys):
    if keys[K_q]:
        sys.exit(0)

if __name__ == "__main__":
    print "Hello World"
