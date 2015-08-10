import fileinput

def main():
	data = []
	f = fileinput.input()
	for lines in f:
		data.append(lines)
	lines = data[1:]	
	for line in lines:
		#print line
		numbers = line.split()
		#print numbers
		sum = int(numbers[0]) + int(numbers[1])
		print sum
	
main()