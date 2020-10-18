def hatebase():
	f = open('hatebase.txt', 'r')
	hatebase = f.read()
	f.close()
	data = hatebase.split('\n')

	return data