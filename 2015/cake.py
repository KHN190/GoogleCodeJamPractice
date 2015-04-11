
def find_all_state(l):
	result = []
	lst = l[:]
	
	if sum(lst) == 1:
		result.append(0)

	for k in range(sum(lst)/2):
		# max time a state can use
		# change state k times
		# cost to change state k times
		prof = max_time(lst) - max_time(break_lst(lst, k)) - k
		# find the best profit
		result.append(prof)
	return result

def max_time(l):
	lst = l[:]
	lst.sort()
	return lst[-1]

def break_lst(l, k):
	lst = l[:]
	lst.sort()
	while k > 0:
		x = lst[-1]/2
		lst[-1] -= x
		lst.append(x)
		lst.sort()
		k -= 1
	return lst

def best_k(result):
	return result.index(max(result))

def best_prof(result):
	return max(result)

def main(fname):

	with open(fname) as fin:
		case = int(fin.readline())
		for i in xrange(case):

			fin.readline()
			rsc = [int(j) for j in fin.readline().split()]
			print rsc

			result = find_all_state(rsc)
			print "\t",result

			k = best_k(result)
			print "\tbest_k:", k

			rsc = break_lst(rsc, k)
			print "\t",rsc
			total_time = max_time(rsc) + k

			print total_time

			# with open("out.txt", "a+") as f:
			# 	f.write("Case #%d: %d" % (i+1, total_time))
			# 	f.write("\n")

fname = "test"
# fname = "small.in"

main(fname)