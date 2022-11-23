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
    #print( mat_r )
    C_x, C_y, C_z = 0, 0, 400
    P_x, P_y, P_z = 0, 0, 1 
    C = [ C_x, C_y, C_z, 1 ]
    P = ProjPlane( array([ P_x, P_x, P_z, -500 ]), array([1,0,0]), array([0,1,0]) )

    dir = array([0,0,5,1])
    mat_trx = matrix_translation_3D_homog( [5,0,0] )
    mat_trx1 = matrix_translation_3D_homog( [-5,0,0] )
    mat_try = matrix_translation_3D_homog( [0,5,0] )
    mat_try1 = matrix_translation_3D_homog( [0,-5,0] )

    rot_dir = (0,1,0)
    stepnum = 500
    theta = 2*pi*stepnum**-1

    rot_center = (0,0,-50,1)
    mat_rot = matrix_rotation_3D_homog( theta, n = rot_dir, C = rot_center )
    mat_rot1 = matrix_rotation_3D_homog( -theta, n = rot_dir, C = rot_center )

    for i in range( 3*stepnum ):
        ph_proj = perspective_projection_ph_onto_plane( fig, C, P.coord )
        draw_ph_homog_plane( screen, ph_proj, P, color = 255 )
        
        pygame.display.flip( )

        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and
                                 event.key == K_ESCAPE):
             break

        pygame.time.delay( 20 )
        draw_ph_homog_plane( screen, ph_proj, P, color = 0 )

        P.rotate( rot_dir, theta, (0,0,0,1))
        C = C@mat_rot
        
        print( "C: ", C, "P: ", P.coord )
