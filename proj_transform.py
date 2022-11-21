from numpy import *

class ProjPlane:
    coord: []
    x0: []
    y0: []

    def __init__( self, coord, x0, y0 = [] ):
        self.coord = coord
        self.x0 = x0 
        self.y0 = y0
    
    def coordinates_of_point( self, Q ):
        proj = perspective_projection_matrix( [coord[0], coord[1], coord[2], 0 ], 
                                                [coord[0], coord[1], coord[2],0] )
        Q0 = Q@proj
        Q0 = [ Q0[0], Q0[1], Q0[2] ]
        return dot( Q0, self.x0 ), dot( Q0, self.y0 )

    def rotate( self, rot ):
        self.coord = self.coord@rot 
        print( rot[[0,1,2]][[0,1,2]] )
        self.x0 = self.x0@rot[ix_([0,1,2],[0,1,2])]
        self.y0 = self.y0@rot[ix_([0,1,2],[0,1,2])]
    
    def translate( self, trans ):
        self.coord = self.coord@trans


def perspective_projection_matrix( C, P ):    
    return array( transpose( matrix( P.coord ))*matrix( C ) - dot( P.coord, C )*identity( 4 ))


def matrix_rotation_3D_homog( theta, n = (1,0,0) ):
    norm = sqrt(n[0]**2 + n[1]**2 + n[2]**2)
    n /= array(norm) 
    nn = transpose( matrix( n ))*matrix( n )
    nx = array( [[0,-n[2],n[1]], 
                 [n[2],0,-n[0]],
                 [-n[1],n[0],0]])
    mat = pad( array( cos(theta)*identity( 3 )+sin(theta)*nx+(1-cos(theta))*nn ), [(0,1)] )
    mat[3,3] = 1
    return mat

def matrix_translation_3D_homog( vec ):
    mat = identity( 4 )
    mat[3,0] = vec[0]
    mat[3,1] = vec[1] 
    mat[3,2] = vec[2]
    return mat
    
