def feb(n):
	a, b = 0,1
	result=[]
	while(a<n):
		result += [ a ] #result.append(a)
		a,b = b, a+b
	return result

feb=feb(23)
print(feb)