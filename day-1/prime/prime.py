def generate_prime ():
	A={}
	x=2
	while true:
		if x not in A:
			yield x
			A[x*x]=[x]
			
		else:
			for y in A[x]:
				A.setdefault(y+x, []).append (p)
			del A[x]
		x += 1
		print x

