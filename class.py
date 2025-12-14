import sys


def main() :
	try:
		n = int(sys.stdin.readline())
	except:
		return

	l = [0] * 10001

	for _ in range(n) :
		try:
			x = int(sys.stdin.readline())
			l[x] += 1
		except :
			continue


	for i in range(1, 10001) :
		if l[i] > 0 :
			for _ in range(l[i]) :
				print(i)





main()