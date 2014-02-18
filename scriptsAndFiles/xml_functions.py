import str_functions
import xml

def loadXML(file):
	openTags = 0 				#Número de etiquetas de apertura en cada iteración. Al final el número debería ser cero
	init = 0
	currentXML = None
	child = 0
	parent = 0
	iteration = 0
	while True:
		line = file.readline()
		if len(line) == 0:			#Longitud 0 significa EOF
			break
		str = line.strip(' \n\t')	#Elimina caracteres antes y después del objeto de tipo string line

		#Verifica si es una etiqueta de cierre automático
		if(str[0:1] == '<' and str[-2:] == '/>'):
			pair = str_functions.processLine(str, 'selfClosingTag')	#Recupera una tupla que contiene el mombre de la etiqueta sus atributos
			child = xml.XML(parent = currentXML, tagName = pair[0], attributes = pair[1])	#Crea un nuevo xml hijo
			currentXML.addChild(child)	#Se agrega un nuevo xml hijo al xml actual
		#Verifica si es una etiqueta de cierre
		elif(str[0:2] == '</'):
			openTags-=1
			if(currentXML.getParent() != 'noParent'):	#Si el xml hijo posee un padre, retorna la referencia a éste
				currentXML = currentXML.getParent()		#El padre del xml hijo se convierte en el xml actual.
		#Verifica si es una etiqueta de apertura
		elif(str[0:1] == '<'):
			pair = str_functions.processLine(str, 'openingTag')	#Recupera una tupla que contiene el mombre de la etiqueta sus atributos
			if init == 0 :	#Si es la primera vez que se crea un objeto de la clase xml
				currentXML = xml.XML(tagName = pair[0], attributes = pair[1])
				init = 1
			else:	#Si no es la primera vez que se crea un objeto xml
				child = xml.XML(parent = currentXML, tagName = pair[0], attributes = pair[1])	#Crea un nuevo hijo xml
				currentXML.addChild(child) #Se agrega un nuevo xml al xml actual
				currentXML = child 	#El xml hijo se convierte en el xml actual
			openTags+=1
		#Si no es ninguno de los casos anteriores, se trata del contenido del xml
		else:
			currentXML.addContent(line)	#Se agrega contenido al xml
	return currentXML

def getDBID(deviceID, devices):
	for device in devices.getChildren():
		attribs = device.getAttributes()
		if attribs['id'] == deviceID:
			return device
			break
	return None

def getCapabilityValue(capabilityName, devices, deviceID = None, device = None):
	if(deviceID != None):
		device = getDBID(deviceID, devices)
	groups = device.getChildren()
	if(groups!= 'noChildren'):
		for group in groups:
			for capability in group.getChildren():
				attribs=capability.getAttributes()
				if attribs['name'] == capabilityName:
					return attribs['value']
	fall_back = device.getAttributes()['fall_back']
	if fall_back!='root':
		return getCapabilityValue(capabilityName, devices, deviceID = fall_back)
	return None

def getDevicesWithCapVal(capabilityName, devices, value = None):
	selected = []
	capValue = None
	for device in devices.getChildren():
		capValue = getCapabilityValue(capabilityName,devices, device = device)
		if (capValue!= None and capValue == value):
			selected.append(device)
	return selected