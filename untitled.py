list = [1,2,3,5,2,3,34,6,3,1,32,63,45,34,22]
for i in list.copy().items():
	if i % 2 == 0 :
		del list[i]
print(i)