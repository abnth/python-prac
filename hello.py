class sayHello:
	def __init__(self,name):
		self.name=name
	def hello(self):
		print "Hello ",self.name

sh=sayHello("anurag")
sh.hello()
