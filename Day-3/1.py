f = open("input.txt", "r")

priority_dict = {'a':1, 'A': 27}

ans = 0

def priority(x):
	if (x.islower()):
		return (priority_dict['a'] + ord(x) - ord('a'))
	elif (x.isupper()):
		return (priority_dict['A'] + ord(x) - ord('A'))



def check(a, b):
	for i in a:
		if i in b:
			return priority(i)

for x in f:
	n = len(x.replace("\n", ""))
	n_half = n//2
	# print(n, n_half)
	a, b = x[0:n_half], x[n_half:n]
	# print(a, b)

	ans += check(a, b)

print(ans)