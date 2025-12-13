def cal(nl) :
	m = max(nl)
	aver = 0
	for i in nl :
		aver += i / m * 100
	print(aver / len(nl))


def main() :
	input()
	x = list(map(int,input().split()))
	cal(x)


main()