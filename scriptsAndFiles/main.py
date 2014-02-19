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
'''
selected = getDevicesWithCapVal('colors', devices, value = '16777216')
for device in selected:
	print('device:', device.getAttributes()['id'], '--- fallback:', device.getAttributes()['fall_back'])
'''

#Obtiene los dispositivos cuyo año de lanzamiento fue 2000.
'''selected = devicesReleasedOn(devices, value = '2000')
print('Cantidad de dispositivos liberados en el 2000:', len(selected))
for pair in selected:
	print('device:', pair[0].getAttributes()['id'],'--- date:', pair[1], '--- fallback:', pair[0].getAttributes()['fall_back'])
'''
#Obtiene una lista con los antepasados de un dispositivo(incluyendo dicho dispositivo).
'''hierarchy = getForefathers('sanyo_scp3200_ver1', devices, [])
i = 1
for device in hierarchy:
	print(i,'-',device.getAttributes()['id'])
	i+=1
'''
#pause = input('Enter to finish...')