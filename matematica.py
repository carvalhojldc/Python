class Matematica(object):
	def __init__(self, x=0):
		self.x = x
	def fatorial(self, numb):
		if numb == 1:
			return 1
		return numb*self.fatorial(numb-1)
		

mat = Matematica()

fat = int(raw_input('Fatorial de? '))
print "Resultado =", mat.fatorial(fat)
