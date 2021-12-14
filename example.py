# This example demonstrates usage of the surface area calculator.
# Format: SurfaceArea(shape,length,width,height)

# Import the surfacearea.py file
from surfacearea import *


# Create an object with a value equal to the surface area of a cube
test1 = SurfaceArea('cube',50,50,100)


# Print the cube surface area
print(test1.surface_area)


# Create an object with a value equal to the surface area of a sphere
test2 = SurfaceArea('sphere',100,100,100)


# Print the cone surface area
print(test2.surface_area)
