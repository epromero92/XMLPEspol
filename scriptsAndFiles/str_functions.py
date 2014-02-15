spaces =' \n\t'

def getBef(str, chars):
	name = ''
	for char in str:
		if(char in chars):
			break
		else:
			name = name + char
	rest = str[len(name):]
	return(name, rest)

def addReg(dictionary, key, value):
	if(dictionary == ''):
		if(value=='""'):
			dictionary={key : ''}
		else: 
			dictionary={key : value}
	else:
		if(value =='""'):
			dictionary[key] = ''
		else:
			dictionary[key] = value
	return dictionary

def getTagNameAttribs(str):
	rest = str.strip('<>')
	name = ''
	attribs = ''
	pair = getBef(rest, spaces)
	name = pair[0]
	rest = pair[1]
	rest = rest.strip(spaces)
	while(len(rest)!=0):
		pair = getBef(rest,'=')
		key = pair[0]; key = key.strip()
		rest = pair[1].strip(spaces + '=')
		pair = getBef(rest,spaces)
		value = pair[0]; value = value.strip()
		rest = pair[1].strip(spaces)
		attribs = addReg(attribs, key, value)	
	return (name, attribs)

#Test
print(getTagNameAttribs('<tagName>'))
print(getTagNameAttribs('<tagName k1="va1" k2="va2" k3="">'))