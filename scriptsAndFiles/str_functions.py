spaces =' \n\t'

'''Obtiene la subcadena contenida en str que se encuentra antes de la primera aparición 
de un caracter perteneciente a un conjunto de caracteres especiales(chars)'''
#getBefore :: str -> str ->(str, str)
def getBefore(str, chars):
	name = ''
	for char in str:			#Por cada substring de longitud 1 en str
		if(char in chars):		#Si el substring se encuentra en la cadena de caracteres límite
			break				#terminar el lazo for
		else:					#Caso contrario
			name = name + char 	#Agregar el substring al objeto name
	rest = str[len(name):]		#El objeto rest contiene el substring de str que no contiene a name
	return(name, rest)

'''Agrega un nuevo par key/value a un objeto de clase dict (dictionary)'''
# addRegg :: dict -> str -> str -> dict
def addKeyValue(dictionary, key, value):
	if(value =='""'):			#Si el valor es ""
		dictionary[key] = ''	#Se asigna como valor una cadena vacía
	else:						#Caso contrario
		dictionary[key] = value #Se asigna como valor el objeto value
	return dictionary

'''Recibe una línea de código xml, la procesa y retorna el nombre de la etiqueta y los atributos'''
#processLine :: str -> str ->(str, dict)
def processLine(str, kindOfTag):
	rest = str.strip('<>' + spaces)			#Elimina '<' al inicio de la línea y '>' al final de la línea y posibles espacios en blanco
	name = ''
	attribs = {}							#Se inicializa la lista de atributos con un diccionario vacío
	if kindOfTag == 'selfClosingTag':
		rest = rest.rstrip('/')				#Elimina '/' a final de la línea
	pair = getBefore(rest, spaces)			#Retorna una tupla con el nombre y el resto del primer parámentro y lo referencia con la variable pair
	name = pair[0]							#Referencia el primer elemento de la tupla a la variable name
	rest = pair[1]							#Referencia el segundo elemento de la tupla a la variable rest
	rest = rest.strip(spaces)				#Elimina los espacios antes y después de la cadena
	while(len(rest)!=0):
		pair = getBefore(rest,'=')			#Recupera la clave y el resto de la cadena
		key = pair[0]; key = key.strip()	#Elimina posibles espacios antes y despues de la clave
		rest = pair[1].strip(spaces + '=')	#Elimina posibles espacios e '=' al inicio y final de la cadena
		pair = getBefore(rest,spaces)		#Recupera el valor y el resto de la cadena
		value = pair[0]; value = value.strip()#Elimina posibles espacios antes y despues del valor
		rest = pair[1].strip(spaces)		#Elimina posibles espacios e '=' al inicio y final de la cadena
		attribs = addKeyValue(attribs, key.strip(), value.strip('"'))#agrega un nuevo atributo a la lista de atributos
	return (name, attribs)

#Tests
'''
print(processLine('<tagName>',''))
print(processLine('<tagName k1="va1" k2="va2" k3="">',''))
'''

