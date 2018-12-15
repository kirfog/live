import numpy
z = 5
cells = numpy.random.randint(2, size=(z, z))
print(cells)


def tern(cells):
	z=len(cells)
	nextcells = numpy.random.randint(1, size=(z, z))
	a = numpy.random.randint(1, size=(z+2, z+2))
	b = numpy.random.randint(1, size=(z+2, z+2))

	for x in range(0, z):
		for y in range(0, z):
			a[x+1,y+1] = cells[x,y]

	for x in range(1, z+1):
		for y in range(1, z+1):
			c = 0
			for i in range(x-1, x+2):
				for j in range(y-1, y+2):
					if not (i == x and j == y):
						c = c + a[i,j]
			if a[x, y] == 0 and c == 3:
				b[x, y] = 1
			elif(a[x,y] == 1 and c > 3) or (a[x,y] == 1 and c < 2):
				b[x, y] = 0
			else:
				b[x, y] = a[x, y]

	for x in range(0, z):
		for y in range(0, z):
			nextcells[x,y] = b[x+1,y+1]

	return(nextcells)



for i in range(1,21):
	cells = tern(cells)
	print(cells)