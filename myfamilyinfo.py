class myfamily:
	pass
	def __init__(self,name,age,phonumb,state):
		self.name = name
		self.age = age
		self.phonumb = phonumb
		self.state = state
	def describe(self):
		return 'His/Her name is {} and he/she is at {}. He/She goes by the phone number of {}. And he/she is {}'.format(self.name,self.age,self.phonumb,self.state)

Atam = myfamily('Aman',50,'0996557750045','businessman')
Apam = myfamily('Jumagul',41,'0996555082705','housewife')
Men = myfamily('Asylturatbek',20,'0996500750045','student')
Ukam1 = myfamily('Janara',18,'0996702750045','student')
Ukam2 = myfamily('Esentur',16,'0996999838823','student')
Ukam3 = myfamily('Madina',9,'Na','pupil')
Ukam4 = myfamily('Akpolot',1,'Na','baby')

print(Ukam4.describe())
