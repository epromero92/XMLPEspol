import str_functions
import xml

f = open('wurfl-2.3m.xml')
openTags = 0
init = 0
currentXML = None

while True:
	child = 0
	parent = 0
	line = f.readline()
	if len(line) == 0:
		break
	str = line.strip(' \n\t')
	if(str[0:2] == '</'):
		openTags-=1
		if(currentXML.getParent() != 'noParent' ):
			currentXML = currentXML.getParent()
	elif(str[0:1] == '<' and str[-2:] == '/>'):
		pair = str_functions.getTagNameAttribs(str, 'selfClosingTag')
		child = xml.XML(parent = currentXML, tagName = pair[0], attributes = pair[1])
		currentXML.setChildren(child)
	elif(str[0:1] == '<'):
		pair = str_functions.getTagNameAttribs(str, 'openingTag')
		if init == 0 :
			currentXML = xml.XML(tagName = pair[0], attributes = pair[1])
			init = 1
		else:
			child = xml.XML(parent = currentXML, tagName = pair[0], attributes = pair[1])
			currentXML.setChildren(child)
			currentXML = child
		openTags+=1
	else:
		print('Not identified yet', end = '')

f.close()

#Test
group = currentXML.getChildren()[0].getChildren()[0].getChildren()
for capability in group:
	print('parent:', capability.getParent().getTagName(), '- child:', capability.getTagName(), ' - attributes:', capability.getAttributes())


