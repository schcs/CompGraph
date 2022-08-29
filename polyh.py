# The polyhedron class

from numpy import *
from affine_transform import matrix_projection_to_plane
from plot import is_visible


class Polyhedron:

    points = [] # the list of points 
    edges = [] # the list of segments
    faces = [] # the list of faces
    dim = 3 # if 2D or 3D
    type = "affin" # affin ou projective

    def __init__( self, points, edges, faces = [], dim = 3, type = "affin" ):
        self.points = points
        self.edges = edges 
        self.faces = faces


class Polygon:

    points = [] # the list of points 
    edges = [] # the list of segments
    dim = 2 # if 2D or 3D
    type = "affin" # affin ou projective

    def __init__( self, points, edges, dim = 2, type = "affin" ):
        self.points = points
        self.edges = edges 


# We define two polyhedra to experiment with 

cube = Polyhedron( [(-100, 100, 100), ( 100, 100, 100),
                          ( 100,-100, 100), (-100,-100, 100),
                          (-100, 100,-100), ( 100, 100,-100),
                          ( 100,-100,-100), (-100,-100,-100)], 
                   [(1,2),(2,3),(3,4),(4,1),(5,6),(6,7),(7,8),(8,5),(1,5),(2,6),(3,7),(4,8)], 
                   [(1,2,3,4,1),(5,6,7,8,5),(1,5,6,2,1),(4,3,7,8,4),(2,6,7,3,2),(1,5,8,4,1)])

square = Polygon( [(50, 100), ( 100, 100),
                     ( 100,50), (50,50)], 
                     [(1,2),(2,3),(3,4),(4,1)], type = "2D" )



gr = 50*(1+sqrt(5))

icosa = Polyhedron( [(0,100,gr), (0,-100,gr), (0,100,-gr), (0,-100,-gr),
                    (100,gr,0), (-100,gr,0), (100,-gr,0), (-100,-gr,0),
                    (gr,0,100), (gr,0,-100), (-gr,0,100), (-gr,0,-100)],
                    [(1,2),(1,5),(1,6),(1,9),(1,11), (2,7),(2,8),(2,9),(2,11),
                     (3,4),(3,5),(3,6),(3,10),(3,12),
                     (4,7),(4,8),(4,10),(4,12),
                     (5,6),(5,9),(5,10),
                     (6,11),(6,12),
                     (7,8),(7,9),(7,10),
                     (8,11),(8,12),(9,10),(11,12) ] )


def transform_ph( ph, matrix ):
    return Polyhedron( [ p@matrix for p in ph.points ], ph.edges, ph.faces, ph.type )


def project_ph_onto_plane( ph, n ):

    mat = matrix_projection_to_plane( n )

    new_ph = Polyhedron( [], [], [] )
    new_ph.points = [ p@mat for p in ph.points ]
    new_ph.edges = ph.edges
    new_ph.faces = [ f for f in ph.faces if is_visible( ph, f )]
    return new_ph
 