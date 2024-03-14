import pyvista as pv
from pyvista import examples
from models import *

pl = pv.Plotter()
pl.add_mesh(body, color='silver', specular=1.0, specular_power=10)
pl.add_mesh(wing1, color='lightblue', specular=1.0, specular_power=10)
pl.add_mesh(wing2, color='lightblue', specular=1.0, specular_power=10)

cubemap = examples.download_cubemap_space_16k()
_ = pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)

pl.add_mesh(earth, texture=earth_texture, smooth_shading=False)
pl.show()
