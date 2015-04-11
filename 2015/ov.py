fname = "large.in"

with open(fname, "r") as fin:
	case = int(fin.readline())
	for i in xrange(case):
		s = [int(num) for num in fin.readline().split()[1]]
		print s
		cost = 0
		for k in range(1, len(s)):
			if sum(s[0:k]) < k:
				c = k - sum(s[0:k])
				cost += c
				s[0] += c # friend here
				print "cost increase: ", cost
		print 
		msg = "Case #%d: %d" % (i+1, cost)
		with open("out.txt", "a+") as fout:
			fout.write(msg)
			fout.write("\n")