def method_friendly_decorator(method_to_decorate):
	def wrapper(self, x):
		x = x -3
		return method_to_decorate(self,x)
	return wrapper

class Lucy(object):
	def __init__(self):
		self.age = 32
	@method_friendly_decorator
	def sayYourAge(self, lie):
		print("Мне {0}, а ты бы сколько дал?".format(self.age +lie))
l = Lucy()
print(l.sayYourAge(-3))