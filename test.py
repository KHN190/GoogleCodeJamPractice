class table():
	
	def __init__(self):
		self.case = 0
		self.tbl = []

	def readrun(self, name):
		with open(''.join(['A-',name,'-practice.in'])) as f:
			self.case = int(f.readline())
			self.life = self.case
			while(self.life):
				# read size and success K
				size = f.readline().split()
				succ = int(size[1])
				size = int(size[0])
				# there is the table
				self.createTbl(f, size, succ)
				# finish the case
				self.life -= 1

	def rotate(self, size):
		tbl = []
		for i in xrange(size):
			line = []
			for j in xrange(size):
				# rotate
				line.append(self.tbl[size-1-j][i])
			tbl.append(line)
		self.tbl = tbl

	def grav(self, size, colm):
		while '.' in colm:
			colm.remove('.')
		colm = ['.'] * (size-len(colm)) + colm
		return colm

	def adjust(self, size):
		tbl = []
		for i in xrange(size):
			colm = self._makecolm(i, size)
			# gravity takes effect
			colm = self.grav(size, colm)
			# restore the column
			for j in xrange(size):
				self.tbl[j][i] = colm[j]

	def show(self, size):
		for i in xrange(size):
			print ''.join(self.tbl[i])

	def _makecolm(self, i, size):
		colm = []
		for j in xrange(size):
			colm.append(self.tbl[j][i])
		print "column", ''.join(colm)
		return colm

	def _makerdiag(self, i, j, size):
		x = i; y = j; diag = []
		while x < size and y < size:
			diag.append(self.tbl[x][y])
			x += 1; y += 1
		return diag

	def _makeldiag(self, i, j, size):
		x = i; y = j; diag = []
		while x >= 0 and y < size:
			diag.append(self.tbl[x][y])
			x -= 1; y += 1
		return diag

	def win(self, size, succ):
		rwin, bwin = 0, 0
		# check row
		for row in self.tbl:
			if (rwin == 0):
				if ''.join(['R'] * succ) in ''.join(row): rwin = 1
			if (bwin == 0):
				if ''.join(['B'] * succ) in ''.join(row): bwin = 1
		# check column
		for i in xrange(size):
			# find column
			colm = self._makecolm(i, size)
			# find if anybody win
			if (rwin == 0):
				if ''.join(['R'] * succ) in ''.join(colm): rwin = 1
			if (bwin == 0):
				if ''.join(['B'] * succ) in ''.join(colm): bwin = 1
		# check diagnosis
		for i in xrange(size):
			for j in xrange(size):
				# right diagnosis
				rdiag = self._makerdiag(i, j, size)
				if (rwin == 0):
					if ''.join(['R'] * succ) in ''.join(rdiag): rwin = 1
				if (bwin == 0):
					if ''.join(['B'] * succ) in ''.join(rdiag): bwin = 1
				# left diagnosis
				ldiag = self._makeldiag(i, j, size)
				if (rwin == 0):
					if ''.join(['R'] * succ) in ''.join(ldiag): rwin = 1
				if (bwin == 0):
					if ''.join(['B'] * succ) in ''.join(ldiag): bwin = 1
		return rwin, bwin

	def write(self, rwin, bwin):
		with open("out", "a+") as f:
			if rwin == 1 and bwin == 1:
				msg = ': Both'
			if rwin == 0 and bwin == 0:
				msg = ': Neither'
			if rwin == 1 and bwin == 0:
				msg = ': Red'
			if rwin == 0 and bwin == 1:
				msg = ': Blue'
			f.write("Case #"+str(self.case-self.life+1)+msg+"\n")

	def createTbl(self, f, size, succ):
		for i in xrange(size):
			self.tbl.append(f.readline().strip())
		# and we do rotate
		self.rotate(size)
		# and we adjust
		self.adjust(size)
		# and find winner
		rwin, bwin = self.win(size, succ)
		self.write(rwin, bwin)
		# clear up
		self.tbl = []

t = table()
t.readrun('large')