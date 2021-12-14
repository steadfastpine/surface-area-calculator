

#import the math library for pi usage
import math


# define the SurfaceArea class
class SurfaceArea:
	
	def __init__(self,shape,length,width,height):

		self.shape=shape
		self.length=length
		self.width=width
		self.height=height

		if shape == 'cube':
			self.surface_area=2*((length * width)+(length * height)+(width * height))


		if shape == 'sphere':
			radius=width/2
			self.surface_area=4*math.pi*(radius**2)







