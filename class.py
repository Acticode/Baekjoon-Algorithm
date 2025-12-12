def cal(nl) :
	h = 0
	for i in range(len(nl)) :
		h += ( ord(nl[i]) - ord('a') + 1 )  * (31 ** i)
	if h >= 1234567891 :
		h %= 1234567891
	print(h)


def main() :
	input()
	x = input()
	cal(x)


main()