from pygame.locals import *
import pygame.draw
import pygame.time
from math import sin, cos
from numpy import sum
from numpy import *

from polyh import *
from lin_alg import *
from affine_transform import *
from plot import *


if __name__ == "__main__": 
    pygame.init()
    screen = pygame.display.set_mode((600,480),HWSURFACE|DOUBLEBUF)

    fig = cube 
    mat_r = matrix_infinitesimal_rotation_3D( .02, (-1,1,1))

    while True:
        #mat_r = matrix_rotation_3D( .01, (-1,1,1))
        fig = transform_ph( fig, mat_r )
        ph_proj = project_ph_onto_plane( fig, [0,0,1])
        draw_ph( screen, ph_proj, color = (255,255,255) )

        pygame.display.flip( )

        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and
                                 event.key == K_ESCAPE):
             break
        
        pygame.time.delay( 20 )
        draw_ph( screen, ph_proj, color = 0 )
        
