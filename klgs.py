from random import randrange
for i in range(0,200):
        r = str(randrange(0,999*999))
	r += '.txt'
	with open(r,'w') as f:
		f.write(str(randrange(0,9999*9999))*999999)
