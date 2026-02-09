def main():
	n = int(input())
	print(calculate(n))

def helper(s):
	if len(s) == 0:
		return 1
	num = int(s[0])
	if num == 0:
		return helper(s[1:])
	elif num == 1:
		return 2**(len(s) - 1) + helper(s[1:])
	elif num >= 2:
		return 2**len(s) 
	else:
		assert(False)

def calculate(n):
	return helper(str(n)) - 1

main()
#print(calculate(13402))