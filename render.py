import pyvista as pv
#imports pyvista, the rendering thing
from pyvista import examples
#imports the "examples" so the earth model can be used
from attributes import *
import skyfield
from skyfield.api import EarthSatellite
from skyfield.api import load, wgs84

pl = pv.Plotter()
#creates a space for the 3d models to be plotted

def satellite_model(x,y,z):
    body = pv.Cube(x_length = 150, y_length = 150, z_length=150, center=(x,y,z))
    #creates the "body" of the satellite with specified center
    wing1 = pv.Cube(x_length=450, y_length=148, z_length=52.5,center=(x,y,z))
    #creates one "wing" of the satellite
    pl.add_mesh(body, color='silver', show_edges=5, edge_color='darkgrey', specular=1.0, specular_power=10)
    pl.add_mesh(wing1, color='lightblue', show_edges=5, edge_color = 'darkgrey', specular=1.0, specular_power=10)
    #adds the object to the 3d space


def render(URL2):
    earth = examples.planets.load_earth(radius=6371)
    #creates the earth with it's set radius
    earth_texture = examples.load_globe_texture()
    #imports earth texture
    pl.add_mesh(earth, texture=earth_texture, smooth_shading=False)
    #adds the earth, with the earth texture

    tempData = load.tle_file(URL2, reload=True)
    attribute_refresh(len(tempData),URL2)
    numb_Sat = len(coords)
    count_sat = 0
    temp_sat = ''
    temp_satCoord = ''
    while count_sat < numb_Sat:
    #iterates through all satellites, picks the name of the satellite from bigData
    #then looks the name up in the dictionary "coords", then seperates the coordinates
    #into three bits, and then calls the function satellite_models with those coordinates
        temp_sat = tempData[count_sat]
        temp_satCoord = coords[temp_sat.name,temp_sat.epoch]
        x = temp_satCoord[0]
        y = temp_satCoord[1]
        z = temp_satCoord[2]
        satellite_model(x,y,z)
        count_sat = count_sat + 1
    cubemap = examples.download_cubemap_space_16k()
    #downloads the "space" background {from NASA}
    _ = pl.add_actor(cubemap.to_skybox())
    #makes it an "actor" so it can be added to the skybox
    pl.set_environment_texture(cubemap, True)
    #adds it as a "cubemap" texture
    #menu()
    pl.view_vector((9000, 0, 0))
    pl.show()
    #renders the plotted items
