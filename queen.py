def queens(num=8, state=()):
	for pos in range(num):
		# 0-7
		if not cf(state, pos):
			if len(state) == num - 1:
				yield (pos,)
			else:
				for r in queens(num, state + (pos,)):
					yield(pos,) + r

def cf(state, nextx):
	nexty = len(state)
	for i in range(nexty):
		if(abs(state[i] - nextx)in(0, nexty - i)):
			return True
	return False
def test():
	print(list(queens(4)))
	input()

if __name__ == '__main__':test()
