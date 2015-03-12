import re

class alien:

	def __init__(self, fname):
		self.words, self.tests = [], []
		with open("A-"+fname+"-practice.in") as f:
			init = f.readline().split()
			(low, dis, self.case) = [int(i) for i in init]
			for i in xrange(dis):
				self.words.append(f.readline().strip())
			for i in xrange(self.case):
				self.tests.append(f.readline().strip())
		self.life = self.case

	def run(self):
		for test in self.tests:
			cnt = 0
			for word in self.words:
				if re.match(self.pattern(test), word):
					cnt += 1
			self.life -= 1
			self.write(''.join(["Case #%d: %d" % (self.case-self.life, cnt)]))

	def write(self, msg):
		with open("out", "a+") as f:
			f.write(''.join([msg,"\n"]))

	def pattern(self, test):
		# get pattern
		test = test.replace("(", "[")
		test = test.replace(")", "]")
		return test

a = alien("large")
a.run()