class A:
    def __init__(self):
        self.a = 5




def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

#print (fact(5))

def fibo(n):
	List = [0,1]
	i = 0
	if n < 3:
		return List[:n]
	while i < n-2:		 
		List.append(List[-1] + List[-2])
		i += 1
	return List

			

#print (fibo(8))

def matrix_inverse():
	A = [[11,12],[21,22],[31,32]]
	B = list()
	for i, ele in enumerate(A[0]):
		B.append(list())
	print (B)	
	for i, row in enumerate(A):
		for j, ele in enumerate(row):
			B[j].append(A[i][j])
	print(B)
	
#matrix_inverse()

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('file')
# parser.add_argument('owner_id')
# parser.add_argument('-r', '--row_list')
# parser.add_argument('-s', '--start_row', type=int)
# args = parser.parse_args()
# print (args.file)
# print (args.owner_id)
# import pdb; pdb.set_trace()
# l = args.row_list[1:-1]
# l = l.split(",")
# print(int(l[0]))
# print (l)
# print (args)


# def print_pascal_triangle(n=3, i=0):
# 	L, j = "", 0
# 	if n - 1 == i:
# 		return
# 	while j < i:
# 		L = L + str(getBinomialCoeff(i, j)) + " "
# 		j += 1
# 	print(L)
# 	return print_pascal_triangle(n, i + 1)
#
#
# def getBinomialCoeff(i, j):
# 	return facto(i) /(facto(j) * facto(i - j))
#
#
# def facto(r):
# 	if r == 1:
# 		return 1
# 	return r * facto(r - 1)
#
#
# print_pascal_triangle(4)



def stringMingling(a,b):
	if not len(a) and not len(b):
		return ""
	k = a[0] + b[0]
	return k + stringMingling(a[1:],b[1:])

#print (stringMingling("mayur", "patil"))


def superNumber(a):
	from functools import reduce
	print (a)

	if len(a)==1:
		return (a)


	d = reduce(sum, [int(cc) for cc in str( a)])
	print ([int(cc) for cc in str(a)])
	return superNumber(str(d))


#print (superNumber("12345"))
class C:
	def a (self,m):
		print (id(m))
		m.a = 12
		print (id(m))


class B:
	def b(self):
		m = A()
		print(id(m))
		c = C()
		c.a(m)
		print (m.a)
		print(id(m))

bb =B()
#bb.b()


def decorator(fun):
	def inner(*args, **kwargs):
		print ("In decorator")
		print (args)
		print (kwargs)
		return fun (*args, **kwargs)
	return inner

@decorator
def cool(a,b,c,d):
	print ("After decorator")
	print (a)
	print (b)
	print (c)
	print (d)
cool(1,2, c=5,d=6)
