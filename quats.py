from random import random
from numpy import *
from math import acos



class Quaternion:
    def __init__( self, sc, i, j, k ):
        self.sc = sc
        self.i = i
        self.j = j
        self.k = k 
    
    def __mul__( self, q ):
        if type( self ) == type( q ):
            return Quaternion( self.sc*q.sc-self.i*q.i-self.j*q.j-self.k*q.k, 
                     self.sc*q.i+self.i*q.sc+self.j*q.k-self.k*q.j,
                     self.sc*q.j+self.j*q.sc+self.k*q.i-self.i*q.k,
                     self.sc*q.k+self.k*q.sc+self.i*q.j-self.j*q.i )
        else:
            return Quaternion( q*self.sc, q*self.i, q*self.j, q*self.k )

    def __add__( self, q ):
        return Quaternion( self.sc+q.sc, self.i+q.i, self.j+q.j, self.k+q.k )
    
    def conjugate( self ):
        return Quaternion( self.sc, -self.i, -self.j, -self.k )
    
    def conjugate_vec( self, vec ):
        p = Quaternion( 0, vec[0], vec[1], vec[2] )
        p1 = self*p*self.conjugate()
        return array( [p1.i, p1.j, p1.k] )

    def norm( self ):
        return (self.sc**2+self.i**2+self.j**2+self.k**2)**(1/2)


def random_quat( unit = False ):
    q = Quaternion( 2*(random.random()-.5), 2*(random.random()-.5), 2*(random.random()-.5), 2*(random.random()-.5) )

    if  not unit:
        return q

    n = (q.sc**2+q.i**2+q.j**2+q.k**2)**(1/2)
    return Quaternion( q.sc/n, q.i/n, q.j/n, q.k/n )

def slerp( p, q, t ):
    teta = acos( p.sc*q.sc+p.i*q.i+p.j*q.j+p.k*q.k )
    return (p*sin((1-t)*teta)+q*sin(t*teta))*(1/sin(teta))

def srerp( p, q, t ):

    z = p*(1-t)+q*t 
    return z*(z.norm())**-1











