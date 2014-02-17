class XML:
	
	def __init__(self, tagName, parent = 'noParent', attributes = 'noAttributes', children = 'noChildren', content = 'noContent'):
		self.__parent = parent 			#Objeto de la clase string.
		self.__tagName = tagName 		#Objeto de la clase string.
		self.__attributes = attributes 	#Objeto de la clase dict.
		self.__children = children 		#Lista de objetos de la clase XML.
		self.__content = content 		#Objeto de la clase string.

	def __str__(self):
		if(self.__parent == 'noParent'):
			return 'parent: {0}, tagName: {1}, attributes: {2}, children: {3}, content: {4}'.format(self.__parent, self.__tagName, self.__attributes, self.__children, self.__content)
		else:
			return 'parent: {0}, tagName: {1}, attributes: {2}, children: {3}, content: {4}'.format(self.__parent.getTagName(), self.__tagName, self.__attributes, self.__children, self.__content)
	#parent
	def getParent(self):
		return self.__parent #Retorna una referencia al xml Padre
	def setParent(self, parent):
		self.__parent = parent
	parent = property(getParent, setParent)

	#tagName
	def getTagName(self):
		return self.__tagName
	tagName = property(getTagName)	

	#attributes
	def getAttributes(self):
		return self.__attributes
	def setAttributes(self, attributes):
		self.__attributes = attributes
	def addAttribute(self, key, value):
		if self.__attributes =='noAttributes':#Si no se ha creado el diccionario
			self.__attributes = {key:value} #Se crea un diccionario
		else:
			self.__attributes[key] = value#Se agrega un par key/value al diccionario
	attributes = property(getAttributes, setAttributes) 

	#children
	def getChildren(self):
		return self.__children
	def setChildren(self, children):
		self.__children = children
	def addChild(self, child):
		if self.__children == 'noChildren':
			self.__children =[child,]#Se crea una lista de referencias a objetos xml que contiene a los hijos
		else:
			self.__children.append(child)#Se añade una nueva a referencia para un nuevo hijo
	children = property(getChildren, setChildren)

	#content
	def getContent(self):
		return self.__content
	def setContent(self, content):
		self.__content = content
	def addContent(self, content):
		if self.__content == 'noContent':
			self.__content = content
		else:
			self.content = self.__content + content
	content = property(getContent, setContent)
