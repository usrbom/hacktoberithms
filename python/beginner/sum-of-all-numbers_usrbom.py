def test(a,b):
	temp = a if a<=b else b
	if temp==b:
		b = a
		a = temp
	
	# a<=b except when a and b both negative
	if a>=0 and b>=0:
		return a - a*(a+1)/2 + b*(b+1)/2
	elif a<0 and b<0:
		a = -a
		b = -b
		return -1*(b - b*(b+1)/2 + a*(a+1)/2)
	else:
		a = -a
		return - a*(a+1)/2 + b*(b+1)/2

print(test(4,1))
print(test(1,4))
print(test(-1,-4))
print(test(-4,-1))
print(test(4,-1))
print(test(-4,1))
