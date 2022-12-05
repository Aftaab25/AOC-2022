f = open("input.txt", "r")

score = 0

for x in f:
	op, me = x.replace("\n", "").split(" ")
	
	score += {'X': 0, 'Y': 3, 'Z': 6}[me]
	score += {
		('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
		('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
		('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1
	}[(op, me)]

print(score)