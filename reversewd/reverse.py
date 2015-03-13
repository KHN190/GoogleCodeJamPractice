def read(fname):
	with open("".join(["B-",fname,"-practice.in"])) as f:
		return f.readlines()[1:]
def write(lines):
	with open("out", "a+") as f:
		cnt = 1
		for line in lines:
			f.write("Case #%d: " % cnt)
			f.write(" ".join(line))
			f.write("\n")
			cnt += 1
text = [i.split() for i in read("small")]
text = [reversed(i) for i in text]
write(text)