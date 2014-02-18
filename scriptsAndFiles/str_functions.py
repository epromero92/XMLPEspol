spaces =' \n\t'

'''Obtiene la subcadena contenida en str que se encuentra antes de la primera aparición 
de un caracter perteneciente a un conjunto de caracteres especiales(chars)'''
#getBefore :: str -> str ->(str, str)
def getBefore(str, chars):
	name = ''
	for char in str:			#Por cada substring de longitud 1 en str
		if(char in chars):		#Si el substring se encuentra en la cadena de caracteres límite
			break				#terminar el lazo for
		else:					#Taso contrario
			name = name + char 	#Agregar el substring al objeto name
	rest = str[len(name):]		#El objeto rest contiene el substring de str que no contiene a name
	return(name, rest)

'''Obtene la primera subcadena contenida en str que se encuentre entre un par de caracteres especiales.
Dicho caracter es el segundo argumento de la función'''
#getBetween :: str -> str -> (str, str)
def getBetween(str, char):
	word = ''
	flag = 0
	for char in str:
		if char == '"':
			flag+=1
		elif flag == 1:
			word = word + char
	return (word, str[len(word)+2:])

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
		pair = getBetween(rest,'"')		#Recupera el valor y el resto de la cadena
		value = pair[0];					#Se le envía una referencia del primer elemento de la dupla a value
		rest = pair[1].strip(spaces)		#Elimina posibles espacios al inicio y final de la cadena
		attribs[key] = value 				#Agrega un nuevo atributo a la lista de atributos
	return (name, attribs)

#Test
'''
print(processLine('<tagName>',''))
print(processLine('<tagName k1="va1" k2="va2" k3="">',''))
print(processLine('<tagName k1=    "	va1	" k2="	va2" k3=	"">',''))
'''
