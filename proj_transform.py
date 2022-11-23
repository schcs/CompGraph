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

        proj = perspective_projection_matrix( [self.coord[0], self.coord[1], self.coord[2], 0 ], 
                                                [self.coord[0], self.coord[1], self.coord[2],0] )        
        Q0 = Q@proj
        Q0 = [ Q0[0]/Q0[3], Q0[1]/Q0[3], Q0[2]/Q0[3] ]
        return dot( Q0, self.x0 ), dot( Q0, self.y0 )

    def rotate( self, dir, angle, C ):

        projC = C@perspective_projection_matrix( [ self.coord[0], self.coord[1], self.coord[2], 0], 
                    self.coord )
        #print( "projC", projC, "C", C )
        #print( "dist0: ", ( (projC[0]/projC[3]-C[0]/C[3])**2 + (projC[1]/projC[3]-C[1]/C[3])**2 + 
        #                (projC[2]/projC[3]-C[2]/C[3])**2 )**(1/2))
                    
        rot = matrix_rotation_3D_homog( angle, n = dir, C = C )
        rot_orig = matrix_rotation_3D_homog( angle, n = dir )

        self.coord = self.coord@array(transpose( matrix( rot ))**-1) 
        self.x0 = self.x0@rot_orig[ix_([0,1,2],[0,1,2])]
        self.y0 = self.y0@rot_orig[ix_([0,1,2],[0,1,2])]

        assert abs(dot( self.x0, self.y0 )) < 10**-6
        assert abs(dot( self.x0, self.coord[[0,1,2]] )) < 10**-6
        assert abs(dot( self.y0, self.coord[[0,1,2]] )) < 10**-6

        projC = C@perspective_projection_matrix( [ self.coord[0], self.coord[1], self.coord[2], 0], 
                    self.coord )

        print( "dist0: ", ( (projC[0]/projC[3]-C[0]/C[3])**2 + (projC[1]/projC[3]-C[1]/C[3])**2 + 
                        (projC[2]/projC[3]-C[2]/C[3])**2 )**(1/2))
        
    
    def translate( self, trans ):
        self.coord = self.coord@transpose( trans )

        assert abs(dot( self.x0, self.y0 )) < 10**-6
        assert abs(dot( self.x0, self.coord[[0,1,2]] )) < 10**-6
        assert abs(dot( self.y0, self.coord[[0,1,2]] )) < 10**-6

def perspective_projection_matrix( C, P ):    
    return array( transpose( matrix( P ))*matrix( C ) - dot( P, C )*identity( 4 ))


def matrix_rotation_3D_homog( theta, n = (1,0,0), C = (0,0,0) ):

    norm = sqrt(n[0]**2 + n[1]**2 + n[2]**2)
    n /= array(norm) 
    nn = transpose( matrix( n ))*matrix( n )
    nx = array( [[0,-n[2],n[1]], 
                 [n[2],0,-n[0]],
                 [-n[1],n[0],0]])
    mat = pad( array( cos(theta)*identity( 3 )+sin(theta)*nx+(1-cos(theta))*nn ), [(0,1)] )
    mat[3,3] = 1

    if C == (0,0,0):
        return mat
    else:
        trans = matrix( matrix_translation_3D_homog( [C[0]/C[3],C[1]/C[3],C[2]/C[3]] ))
        return array(trans**-1*mat*trans) 

def matrix_translation_3D_homog( vec ):
    mat = identity( 4 )
    mat[3,0] = vec[0]
    mat[3,1] = vec[1] 
    mat[3,2] = vec[2]
    return mat
    
