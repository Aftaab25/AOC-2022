f = open("input.txt", "r")

elf_calories = []
curr = 0

for x in f:
  	if x == "\n":
  		elf_calories.append(curr)
  		curr = 0
  	else:
  		curr += int(x)

elf_calories.sort(reverse=True)

print(elf_calories[0])