from pygame.locals import *
import pygame.draw
import pygame.time

from lin_alg import center
from lin_alg import normal_vector, dot_product


def is_visible( ph, face ):
    p = center( [ ph.points[face[i]-1] for i in range( len(face)-1)]) 
    n = normal_vector( ph.points[face[0]-1],ph.points[face[1]-1], ph.points[face[2]-1], direction = p )
    eye = (0,0,100)
    return dot_product( n, eye ) <= 0


def draw_ph( screen, ph, color = 255 ):

    t = lambda p: (p[0]+300, -p[1]+240 )
    for face in ph.faces:
        for i in range( 1, len(face)):
            pygame.draw.line( screen, color, t(ph.points[face[i-1]-1]), t(ph.points[face[i]-1]) )


def draw_pg( screen, pg, color = 255 ):

    t = lambda p: (p[0]+300, -p[1]+240 )
    for i in range( pg.edges-1 ):
        p1, p2 = pg.edges[i], pg.edges[i+1]
        pygame.draw.line( screen, color, t(pg.points[p1-1]-1), t(pg.points[p2-1]-1) )
