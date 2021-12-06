import sys

s = list(map(int,open(sys.argv[1]).read().split(",")))

t = [1]*300
for i in range(300):
	t[i] = t[i-9] + t[i-7]

a = lambda x: sum(t[x-i] for i in s)

print("Part 1: {:d}".format(a(79)))
print("Part 2: {:d}".format(a(255)))
