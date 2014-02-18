from xml_functions import *

f = open('wurfl-2.3m2.xml')	#Si no se especifica el modo, el modo 'r'ead (lectura) se establece por defecto 
devices = loadXML(f)
f.close()	#Se cierra el archivo

'''Tests'''
#Imprime el nodo devices.
#print(devices)

#Obteniene una referencia al dispositivo con atributo name = "sharp_tqgx12_ver1"
'''device = getDBID('sharp_tqgx12_ver1', devices)
print(device)'''

#Obteniene el valor del capability de nombre "mobile_browser" del dispositivo con atributo name = "browser_opera_mobi_9_7"
'''deviceID = 'browser_opera_mobi_9_7'
capabilityName = 'mobile_browser'
capabilityValue = getCapabilityValue(capabilityName, devices, deviceID = deviceID)
print(deviceID, capabilityName, '+', capabilityValue)'''

#Obtiene los dispositivos que poseen una pantalla de 16777216 colores.
selected = getDevicesWithCapVal('colors', devices, value = '16777216')
for device in selected:
	print('device:', device.getAttributes()['id'], '--- fallback:', device.getAttributes()['fall_back'])