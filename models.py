import pyvista as pv
from pyvista import examples

earth = examples.planets.load_earth(radius=6378.1)
earth_texture = examples.load_globe_texture()

body = pv.Cube(x_length=1000, y_length=1000, z_length=1000,center=(10000, 0, 0))
wing1 = pv.Cube(x_length=2000, y_length=1000, z_length=125,center=(11000,0,0))
wing1.rotate_x(20, inplace=True)
wing2 = pv.Cube(x_length=2000, y_length=1000, z_length=125,center=(9000,0,0))
wing2.rotate_x(30, inplace=True)
