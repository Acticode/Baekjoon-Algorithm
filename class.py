def cal(a, b) :
	if b == 0 :
		return a
	return cal(b, a % b)

def main() :
	x = list(map(int,input().split()))
	gcd = cal(x[1],x[0])
	lcm = int(x[0] * x[1] / gcd)
	print(gcd)
	print(lcm)


main()