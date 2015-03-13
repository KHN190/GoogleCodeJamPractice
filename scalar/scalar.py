def cross(m,n):
	for i,j in zip(m,n):
		yield i*j
def answer(m,n):
	return sum(cross(m,n))
def adjust(vec):
	return sorted(vec[0]), reversed(sorted(vec[1]))
def write(msg):
	with open("out", "a+") as f:
		f.write(msg)
def run(fname):
	with open("".join(["A-",fname,"-practice.in"])) as f:
		case = int(f.readline())
		cnt  = 1
		while case:
			vec = []
			f.readline()
			for i in xrange(2):
				vec.append([int(i) for i in f.readline().split()])
			vec = adjust(vec)
			crs = answer(vec[0], vec[1])
			msg = "Case #%d: %d\n" % (cnt, crs)
			write(msg)
			case -= 1; cnt += 1
run("large")