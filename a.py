from numpy import *
z = 3
#a = zeros((z+2, z+2))
b = zeros((z+2, z+2))

a=array([[0, 0, 0, 0, 0,],
 		 [0, 1, 1, 0, 0,],
 		 [0, 0, 1, 1, 0,],
 		 [0, 1, 1, 0, 0,],
 		 [0, 0, 0, 0, 0,]])

def neib(array,z):
	for x in range(1, z+1):
		for y in range(1, z+1):
			c = 0
			for i in range(x-1, x+2):
				for j in range(y-1, y+2):
					if i != j:
						c = c + a[i,j]
						print(c)
			if a[x, y] == 0 and c == 3:
				b[x, y] = 1
			elif (a[x,y] == 1 and c > 3) or (a[x,y] == 1 and c < 2):
				b[x, y] = 0
			else:
				b[x, y] = a[x, y]
	return b
d = neib(a,z)
print(d)

