f = open("input.txt", "r")

score = 0

for x in f:
	op, me = x.replace("\n", "").split(" ")
	
	score += {'X': 1, 'Y': 2, 'Z': 3}[me]
	score += {
		('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
		('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
		('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3
	}[(op, me)]

print(score)