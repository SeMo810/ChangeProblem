import sys

Changes = [1, 5, 10, 25, 50, 100]

# n is the total change to be make, m is the index of the highest denomination allowed
def change(n, m):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if m < 0 and n >= 1:
		return 0
	return change(n, m - 1) + change(n - Changes[m], m)

# This gets the index for the entered string, or -1 is not correct
def getIndexFromChange(x):
	return {
		1:   0,
		5:   1,
		10:  2,
		25:  3,
		50:  4,
		100: 5
	}.get(x, -1)

def main():
	if len(sys.argv) != 3:
		print("Usage: \"python problem.py amt denom\", amt is number of cents to make change for, demon is highest denomination coin allowed")
	amt = int(sys.argv[1])
	denom = getIndexFromChange(int(sys.argv[2]))
	if denom == -1:
		print("Please enter a correct denomination: 1, 5, 10, 25, 50, or 100")
		sys.exit(-1)
	cnt = change(amt, denom)
	ans = "The number of ways to make change for ${0:.2f} with the highest denomination of {1} cents is {2}."
	ans = ans.format(amt / 100, Changes[denom], cnt)
	print(ans)
	
main()
