from operator import itemgetter

persons = []

while True:
	line = input("> ")
	if not line:
		break
	persons.append(tuple(line.split(',')))

persons = sorted(persons, key=itemgetter(0,1,2))

for person in persons:
	print (','.join(person))

