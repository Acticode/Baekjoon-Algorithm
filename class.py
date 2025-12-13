def cal(f, r) :
	l = [ ([0] * r) for _ in range(f+1) ]
	for i in range(r) :
		l[0][i] = i+1
	for j in range(1, f+1) :
		l[j][0] = l[j-1][0]
		for k in range(r) :
			l[j][k] = l[j][k-1] + l[j-1][k]
	print(l[f][r-1])



def main() :
	x = int(input())
	for i in range(x) :
		floor = int(input())
		room = int(input())
		cal(floor, room)


main()