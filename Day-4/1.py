f = open("sample.txt", "r")

ans = 0

for x in f:
	n = x.replace("\n", "").split(",")
	# range1 = list(range(n[0].split("-")))
	# range2 = list(range(n[1].split("-")))
	
	# range1 = list(range(5))

	range1 = (int(n[0]).split("-"))

	print(range1)

	if range1[0] <= range2[0]:
		if range1[1] >= range2[1]:
			ans += 1

	elif range1[0] >= range2[0]:
		if range1[1] <= range2[1]:
			ans += 1

print(ans)