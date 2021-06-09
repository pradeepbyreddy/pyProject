
def feb(n):
	a, b = 0,1
	result=[]
	while(a<n):
		print(a, end = " ")
		result += [ a ] #result.append(a)
		a,b = b, a+b
	return result

feb=feb(23)
print(feb)
