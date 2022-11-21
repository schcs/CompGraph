from pygame.locals import *
import pygame.draw
import pygame.time
import pygame.key
from math import sin, cos
from numpy import sum
from numpy import *

from polyh import *
from lin_alg import *
from affine_transform import *
from plot import *
from proj_transform import *


if __name__ == "__main__": 
    pygame.init()
    screen = pygame.display.set_mode((600,480),HWSURFACE|DOUBLEBUF)

    fig = cube_homog
    mat_r = matrix_rotation_3D_homog( .01, (-1,1,1))
    print( mat_r )
    C_x, C_y, C_z = 0, 0, 300
    P_x, P_y, P_z = 0, 0, 1 
    C = [ C_x, C_y, C_z, 1 ]
    P = ProjPlane( [ P_x, P_x, P_z, 1 ], [1,0,0], [0,1,0] )

    dir = array([0,0,5,1])

    while True:
        mat_trx = matrix_translation_3D_homog( [5,0,0] )
        mat_trx1 = matrix_translation_3D_homog( [-5,0,0] )
        mat_try = matrix_translation_3D_homog( [0,5,0] )
        mat_try1 = matrix_translation_3D_homog( [0,-5,0] )
        mat_trz = matrix_translation_3D_homog( dir )
        mat_trz1 = matrix_translation_3D_homog( -dir )
        
        mat_rot = matrix_rotation_3D_homog( .1, n = (0,1,0))
        mat_rot1 = matrix_rotation_3D_homog( -.1, n = (0,1,0))

        #fig = transform_ph( fig, mat_r )
        ph_proj = perspective_projection_ph_onto_plane( fig, C, P )
        draw_ph_homog_plane( screen, ph_proj, P, color = 255 )
        
        pygame.display.flip( )

        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and
                                 event.key == K_ESCAPE):
             break

        pygame.time.delay( 20 )
        draw_ph_homog_plane( screen, ph_proj, P, color = 0 )

        keys = pygame.key.get_pressed()
        
        if keys[K_UP]:
            C = C@mat_trz 
            P.translate( mat_trz )
        elif keys[K_DOWN]:
            C = C@mat_trz1
            P.translate( mat_trz1 )
        if keys[K_LEFT]:
            C = C@mat_rot
            P.rotate( mat_rot )
        elif keys[K_RIGHT]:
            C = C@mat_rot1
            P.rotate( mat_rot1 )
        
