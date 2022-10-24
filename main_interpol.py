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
from quats import *


if __name__ == "__main__": 
    pygame.init()
    screen = pygame.display.set_mode((600,480),HWSURFACE|DOUBLEBUF)

    #fig = cube 
    q = random_quat( unit = True )
    p = random_quat( unit = True )
    #theta = acos( q.sc*p.sc + p.i*q.i + p.j*q.j + p.k*q.k )
    #print( "Rotation angle: ", 180*theta/(2*pi), " degrees" )

    #fig_init = project_ph_onto_plane( transform_ph_quat( cube, p ), [0,0,1] )
    fig_end = project_ph_onto_plane( transform_ph_quat( cube, q ), [0,0,1] )
    #draw_ph( screen, fig_init, color = (255,255,0) )
    draw_ph( screen, fig_end, color = (0,255,255) )
    
    t = 0
    while True:
        t += .001
        #mat_r = matrix_rotation_3D( .01, (-1,1,1))
        #fig = transform_ph_quat( fig, q )
        
        p1 = srerp( p, q, t )
        fig = transform_ph_quat( cube, p1 )

        ph_proj = project_ph_onto_plane( fig, [0,0,1])
        draw_ph( screen, ph_proj, color = (255,255,255) )
        #draw_ph( screen, fig_init, color = (255,255,0) )
        draw_ph( screen, fig_end, color = (0,255,255) )
    

        pygame.display.flip( )
        if abs( t-1 )< 0.01:
            break

        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and
                                 event.key == K_ESCAPE):
             break
        
        pygame.time.delay( 10 )
        draw_ph( screen, ph_proj, color = 0 )
        
