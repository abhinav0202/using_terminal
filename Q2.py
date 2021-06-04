#Print Duplicate Numbers 
def duplicate(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated

list1 = [3,5,7,4,1,5,7,3,1,45,6,84,3,5,73,5]
print (duplicate(list1))