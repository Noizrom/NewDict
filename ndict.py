from builtins import dict


class Ndict(dict):
	'''simply a dictionary with dot notation for valid keys'''
	def __init__(self , args='' , **kwargs):
		super(Ndict , self).__init__(args , **kwargs)
		if self:
			for k, v in self.items():
				if k.isidentifier():
					self.__dict__[k] = v

	def __setattr__(self , name , value):
		super(Ndict , self).__setattr__(name , value)
		self[name] = value


