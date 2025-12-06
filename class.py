def cal(num, nl) :
	for i in nl :
		num -= i
	print(num)


def main() :
	x = input()
	y = list(map(int, x.split()))
	cal(x, y)
	