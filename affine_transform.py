from numpy import *

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

def matrix_infinitesimal_rotation_3D( theta, n = (1,0,0) ):

    return identity(3) + theta*array( [[0,-n[2],n[1]], 
                                [n[2],0,-n[0]],
                                [-n[1],n[0],0]])


