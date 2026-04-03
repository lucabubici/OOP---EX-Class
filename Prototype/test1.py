day = 1
total_bugs = 0
while day < 6:
	today_bugs = int(input("How many bugs were caught today?"))
    total_bugs += today_bugs
    day += 1
print(total_bugs)