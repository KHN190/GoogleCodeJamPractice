def pick(cd, ch):
	l = ch
	for i in xrange(len(ch)):
		for j in xrange(i+1, len(ch), 1):
			if ch[i] + ch[j] == cd: 
				return i+1, j+1

def write(m, n, case):
	answer = "".join(["Case #", str(case), ": ", str(m), " ", str(n)])
	with open("out", "a+") as f:
		f.write(answer)
		f.write("\n")

def run(fname):
	with open("".join(["A-",fname,"-practice.in"])) as f:
		case = int(f.readline())
		cnt  = 1
		while case:
			cd = int(f.readline())
			it = int(f.readline())
			ch = [int(i) for i in f.readline().split()]
			# select proper items
			m, n = pick(cd, ch)
			# write answer
			write(m, n, cnt)
			# count cases
			cnt  += 1; case -= 1

run("large")