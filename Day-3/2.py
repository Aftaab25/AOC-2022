f = open("input.txt", "r")

priority_dict = {'a':1, 'A': 27}

def priority(x):
	if (x.islower()):
		return (priority_dict['a'] + ord(x) - ord('a'))
	elif (x.isupper()):
		return (priority_dict['A'] + ord(x) - ord('A'))

def solve(lst):
	# print(lst)
	for i in lst[0]:
		if i in lst[1] and i in lst[2]:
			return priority(i)

counter = 0

lst = []
ans = 0

for x in f:
	if counter != 3:
		lst.append(x)
		# print(lst)
		counter += 1
		if counter == 3:
			# print("here")
			ans += solve(lst)
			lst = []
			counter = 0

print(ans)