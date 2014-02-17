spaces =' \n\t'

'''Obtiene la subcadena contenida en str que se encuentra antes de la primera aparición 
de un caracter perteneciente a un conjunto de caracteres especiales(chars)'''
#getBefore :: str -> str ->(str, str)
def getBefore(str, chars):
	name = ''
	for char in str:	#por cada substring de longitud 1 en str
		if(char in chars): 	#si el substring se encuentra en la cadena de caracteres límite
			break			#terminar el lazo for
		else:				#caso contrario
			name = name + char 	#agregar el substring al objeto name
	rest = str[len(name):]		#el objeto rest contiene el substring de str que no contiene a name
	return(name, rest)

# addRegg :: dict -> str -> str -> dict
'''Agrega un nuevo par key/value a un objeto de clase dict (dictionary)'''
def addReg(dictionary, key, value):
	if(value =='""'):	#si el valor es ""
		dictionary[key] = ''	#se asigna como valor una cadena vacía
	else:				#caso contrario
		dictionary[key] = value #se asigna como valor el objeto value
	return dictionary

def getTagNameAttribs(str, kindOfTag):
	rest = str.strip('<>')
	if kindOfTag == 'selfClosingTag':
		rest = rest[:-2]
	name = ''
	attribs = {}
	pair = getBefore(rest, spaces)
	name = pair[0]
	rest = pair[1]
	rest = rest.strip(spaces)
	while(len(rest)!=0):
		pair = getBefore(rest,'=')
		key = pair[0]; key = key.strip() #Eliminar posibles espacios antes y despues de la clave.
		rest = pair[1].strip(spaces + '=')
		pair = getBefore(rest,spaces)
		value = pair[0]; value = value.strip()
		rest = pair[1].strip(spaces)
		attribs = addReg(attribs, key.strip('"'), value.strip('"'))	
	return (name, attribs)