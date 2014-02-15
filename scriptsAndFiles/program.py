f = open('test1.xml') 
while True:
	line = f.readline()
	if len(line) == 0: 
		break
	str = line.strip(' \n\t')
	if(str[0:2] == '</'):
		print('*****closing tag******', end = '')
	elif(str[0:1] == '<' and str[-2:] == '/>'):
		print('*****selfclosing tag******', end = '')
	elif(str[0:1] == '<'):
		print('*****opening tag******', end = '')
	else:
		print('Not identified yet', end = '')
	print(line)
f.close()