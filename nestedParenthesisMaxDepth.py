#nestedParenthesisMaxDepth.py
# find the maximum depth of nested parenthesis 
# in a string like this s = "(((X))(((Y))))"
# return -1, if number of parenthesis is unbalanced

def findDepth(s):
	maxDepth = 4
	return maxDepth

def main():
	#s = input("Enter the string: ")
	s = "((((Hi))))"
	print "Maximum Depth: "
	print findDepth(s)

if __name__ == '__main__':
	main()