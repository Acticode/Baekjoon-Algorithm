def cal(a, b, v) :

	if v < a :
		return 1

	numer = v - a
	denom = a - b
	return (numer + denom - 1) // denom + 1


def main() :
	x = list(map(int, input().split()))
	print(cal(x[0], x[1], x[2]))


main()