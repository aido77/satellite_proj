import pyvista as pv
from pyvista import examples
#imports the "examples" so the earth model can be used

earth = examples.planets.load_earth(radius=6378.1)
#creates the earth with it's set radius
earth_texture = examples.load_globe_texture()
#imports earth texture

body = pv.Cube(x_length=1000, y_length=1000, z_length=1000,center=(10000, 0, 0))
#creates the "body" of the satellite with these proportions
wing1 = pv.Cube(x_length=2000, y_length=1000, z_length=125,center=(11000,0,0))
#creates one wing of the satellite
wing1.rotate_x(20, inplace=True)
#rotates the wing of the satellite so it doesn't look boring
wing2 = pv.Cube(x_length=2000, y_length=1000, z_length=125,center=(9000,0,0))
#creates wing2
wing2.rotate_x(30, inplace=True)
#also rotates wing2 to be less lame
