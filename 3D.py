import pyvista as pv
#imports pyvista, the rendering thing
from pyvista import examples
#imports the "examples" so the earth model can be used
from datascraper import *
from coords import *

pl = pv.Plotter()
#creates a space for the 3d models to be plotted

def satellite_model(x,y,z):
    body = pv.Cube(x_length = 200, y_length = 200, z_length=200, center=(x,y,z))
    #creates the "body" of the satellite with specified center
    wing1 = pv.Cube(x_length=400, y_length=200, z_length=25,center=(x+200,y,z))
    #creates one "wing" of the satellite
    wing2 = pv.Cube(x_length=400, y_length=200, z_length=25,center=(x-200,y,z))
    #creates the second "wing" of the satellite
    pl.add_mesh(body, color='silver', specular=1.0, specular_power=10)
    pl.add_mesh(wing1, color='lightblue', specular=1.0, specular_power=10)
    pl.add_mesh(wing2, color='lightblue', specular=1.0, specular_power=10)
    #adds the object to the 3d space


numb_Sat = len(bigData) 
count_sat = 0
temp_sat = ''
temp_satCoord = ''
while count_sat < numb_Sat:
    #iterates through all satellites, picks the name of the satellite from bigData
    #then looks the name up in the dictionary "coords", then seperates the coordinates
    #into three bits, and then calls the function satellite_models with those coordinates
    temp_sat = bigData[count_sat]
    temp_satCoord = coords[temp_sat.name]
    x = temp_satCoord[0]
    y = temp_satCoord[1]
    z = temp_satCoord[2]
    satellite_model(x,y,z)
    count_sat = count_sat + 1

earth = examples.planets.load_earth(radius=6378.1)
#creates the earth with it's set radius
earth_texture = examples.load_globe_texture()
#imports earth texture

pl.add_mesh(earth, texture=earth_texture, smooth_shading=False)
#adds the earth, with the earth texture

cubemap = examples.download_cubemap_space_16k()
#downloads the "space" background {from NASA}
_ = pl.add_actor(cubemap.to_skybox())
#makes it an "actor" so it can be added to the skybox
pl.set_environment_texture(cubemap, True)
#adds it as a "cubemap" texture

pl.show()
#renders the plotted items
