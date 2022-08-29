from pygame.locals import *
import pygame.draw
import pygame.time
from math import sin, cos
from numpy import sum
from numpy import *


class Polyhedron:

    points = [] # the list of points 
    edges = [] # the list of segments
    faces = [] # the list of faces
    type = "3D" # if 2D or 3D

    def __init__( self, points, edges, faces = [], type = "3D" ):
        self.points = points
        self.edges = edges 
        self.faces = faces

cube = WireFrame( [(-100, 100, 100), ( 100, 100, 100),
                          ( 100,-100, 100), (-100,-100, 100),
                          (-100, 100,-100), ( 100, 100,-100),
                          ( 100,-100,-100), (-100,-100,-100)], 
                   [(1,2),(2,3),(3,4),(4,1),(5,6),(6,7),(7,8),(8,5),(1,5),(2,6),(3,7),(4,8)], 
                   [(1,2,3,4,1),(5,6,7,8,5),(1,5,6,2,1),(4,3,7,8,4),(2,6,7,3,2),(1,5,8,4,1)])

def cross_product( u, v ):
    return ( u[1]*v[2]-u[2]*v[1], -u[0]*v[2]+u[2]*v[0], u[0]*v[1]-u[1]*v[0] )

def dot_product( u, v ):
    return sum( u[i]*v[i] for i in range( len( u)))

# the normal vector of plane determined by three points
def normal_vector( p1, p2, p3, direction = [] ):
    n = cross_product( p1-p2, p1-p3 )
    
    if direction == []:
        return n

    if dot_product( n, direction ) < 0:
        return array(n)
    else:
        return -array(n)

def is_visible( wf, face ):
    p = center( [ wf.points[face[i]-1] for i in range( len(face)-1)]) 
    n = normal_vector( wf.points[face[0]-1],wf.points[face[1]-1], wf.points[face[2]-1], direction = p )
    eye = (0,0,100)
    return dot_product( n, eye ) <= 0
    
# def center
def center( point_list ):

    l = len( point_list )
    return [ sum( x[0] for x in point_list )/l, 
             sum( x[1] for x in point_list )/l,
             sum( x[2] for x in point_list )/l ] 

                   
gr = 50*(1+sqrt(5))

icosa = WireFrame( [(0,100,gr), (0,-100,gr), (0,100,-gr), (0,-100,-gr),
                    (100,gr,0), (-100,gr,0), (100,-gr,0), (-100,-gr,0),
                    (gr,0,100), (gr,0,-100), (-gr,0,100), (-gr,0,-100)],
                    [(1,2),(1,5),(1,6),(1,9),(1,11), (2,7),(2,8),(2,9),(2,11),
                     (3,4),(3,5),(3,6),(3,10),(3,12),
                     (4,7),(4,8),(4,10),(4,12),
                     (5,6),(5,9),(5,10),
                     (6,11),(6,12),
                     (7,8),(7,9),(7,10),
                     (8,11),(8,12),(9,10),(11,12) ] )

square = WireFrame( [(50, 100), ( 100, 100),
                     ( 100,50), (50,50)], 
                     [(1,2),(2,3),(3,4),(4,1)], type = "3D" )

def draw_wf( screen, wf, color = 255 ):

    t = lambda p: (p[0]+300, -p[1]+240 )
    for face in wf.faces:
        for i in range( 1, len(face)):
            pygame.draw.line( screen, color, t(wf.points[face[i-1]-1]), t(wf.points[face[i]-1]) )


def matrix_projection_to_vector( n ):
    n = array( n )
    n_norm = n[0]**2+n[1]**2+n[2]**2
    return n_norm*array( [n[0]*n, n[1]*n, n[2]*n] )


def matrix_projection_to_plane( n ):
    return identity( 3 ) - matrix_projection_to_vector( n )

def matrix_rotation_3D( theta, n = (1,0,0) ):
    norm = sqrt(n[0]**2 + n[1]**2 + n[2]**2)
    n /= array(norm) 
    nn = transpose( matrix( n ))*matrix( n )
    nx = array( [[0,-n[2],n[1]], 
                 [n[2],0,-n[0]],
                 [-n[1],n[0],0]])

    return array( cos(theta)*identity( 3 )+sin(theta)*nx+(1-cos(theta))*nn )


def transform_wf( wf, matrix ):
    return WireFrame( [ p@matrix for p in wf.points ], wf.edges, wf.faces, wf.type )


def project_wf_onto_plane( wf, n ):

    mat = matrix_projection_to_plane( n )

    new_wf = WireFrame( [], [], [] )
    new_wf.points = [ p@mat for p in wf.points ]
    new_wf.edges = wf.edges
    new_wf.faces = [ f for f in wf.faces if is_visible( wf, f )]
    return new_wf
            
    #return WireFrame( [(p[0],p[1]) for p in wf.points ], wf.edges, type = "2D" )


if __name__ == "__main__": 
    pygame.init()
    screen = pygame.display.set_mode((600,480),HWSURFACE|DOUBLEBUF)

    fig = cube 
    mat_r = matrix_rotation_3D( .01, (-1,1,1))
    mat_p = matrix_projection_to_plane( [0,0,1] )

    while True:
        #mat_r = matrix_rotation_3D( .01, (-1,1,1))
        fig = transform_wf( fig, mat_r )
        wf_proj = project_wf_onto_plane( fig, [0,0,1])
        draw_wf( screen, wf_proj, color = 255 )

        pygame.display.flip( )

        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and
                                 event.key == K_ESCAPE):
             break
        
        pygame.time.delay( 20 )
        draw_wf( screen, wf_proj, color = 0 )
        
