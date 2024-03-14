import pyvista as pv
#imports pyvista, the rendering thing
from models import *
#imports the models, earth and satellites

pl = pv.Plotter()
#creates a 3d space for the models to be rendered in
pl.add_mesh(body, color='silver', specular=1.0, specular_power=10)
#renders the body of the satellite {silver}
pl.add_mesh(wing1, color='lightblue', specular=1.0, specular_power=10)
#renders wing1 of the satellite
pl.add_mesh(wing2, color='lightblue', specular=1.0, specular_power=10)
#renders wing2 of the satellite

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
