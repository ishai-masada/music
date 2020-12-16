class Key:
	
	def __repr__(self):
		return '{scale}'.format(scale = self.scale)
		
	def __init__(self, scale):
		self.scale = scale
		self.third = scale[0], scale[2], scale[4]
