from numpy import *

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

# def center
def center( point_list ):

    l = len( point_list )
    return [ sum( x[0] for x in point_list )/l, 
             sum( x[1] for x in point_list )/l,
             sum( x[2] for x in point_list )/l ] 

