def counter():
	val = 1
	for i in range(10):
		yield val
		val += 1

print(dir(counter()))
