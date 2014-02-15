class XML:
	
	def __init__(self, tagName, parent = 'noParent', attributes = 'noAttributes', children = 'noChildren', content = 'noContent'):
		self.__parent = parent 			#Objeto de la clase string.
		self.__tagName = tagName 		#Objeto de la clase string.
		self.__properties = attributes 	#Objeto de la clase dict.
		self.__children = children 		#Lista de objetos de la clase XML.
		self.__content = content 		#Objeto de la clase string.

	def __str__(self):
		return 'parent: {0}, tagName: {1}, attributes: {2}, children: {3}, content: {4}'.format(self.__parent, self.__tagName, self.__properties, self.__children, self.__content)

	#parent
	def getParent(self):
		return self.__parent
	def setParent(self, parent):
		self.__parent = parent
	parent = property(getParent, setParent)

	#tagName
	def getTagName(self):
		return self.__tagName
	tagName = property(getTagName)	

	#attributes
	def getAttributes(self):
		return self.__properties
	def setAttributes(self, key, value):
		if self.__properties =='noAttributes':
			self.__properties = {key:value}
		else:
			self.__properties[key] = value
	attributes = property(getAttributes, setAttributes)

	#children
	def getChildren(self):
		return self.__children
	def setChildren(self, xmlChild):
		if self.__children == 'noChildren':
			self.__children =[xmlChild,]
		else:
			self.__children.append(xmlChild)
	children = property(getChildren, setChildren)

	#content
	def getContent(self):
		return self.__content
	def setContent(self, content):
		self.__content = content
	content = property(getContent, setContent)


#Tests
xml = XML("tagName")
xml.setAttributes('k1', 'va1')
print(xml.attributes)
xml.setAttributes('k2', 'va2')
print(xml.attributes)
print(xml.__str__())