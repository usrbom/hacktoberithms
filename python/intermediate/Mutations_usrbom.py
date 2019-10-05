def test(input):
	
	list1 = [0]*26
	list2 = [0]*26
	input[0] = input[0].lower()
	input[1] = input[1].lower()
	for x in input[0]:
		list1[ord(x)-97] = list1[ord(x)-97] + 1
	for x in input[1]:
		list2[ord(x)-97] = list2[ord(x)-97] + 1
	for x in range(0,26):
		if list1[x]<list2[x]:
			return False
	return True

print(test(["hello", "Hello"]))
print(test(["hello", "hey"]))
print(test(["Alien", "line"]))
print(test(["CazI", "caz"]))
	