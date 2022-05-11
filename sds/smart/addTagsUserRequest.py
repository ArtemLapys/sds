def addTagsForRequestUser(objectRequestGet):
	# print((objectRequestGet))
	nfc = None
	gps = None
	five_g = None
	jack = None
	allData=objectRequestGet
	platform = allData["radioPlatform"]
	price = allData["rangePrice"]
	diagonal = allData["rangeDiagonal"]
	ram = allData["rangeRam"]
	rom = allData["rangeRom"]
	battery = allData["rangeBattery"]
	processor = allData["rangeProcessor"]
	if 'checkboxFive_g' in allData:
		five_g=allData["checkboxFive_g"]
	if 'checkboxNfc' in allData:
		nfc = allData["checkboxNfc"]
	if 'checkboxGps' in allData:
		gps = allData["checkboxGps"]
	if 'checkboxJack' in allData:
		jack = allData["checkboxJack"]
	sim = allData["radioSim"]
	warranty = allData["rangeWarranty"]
	
	resultTags = []
	
	if platform == 'Android':
		resultTags.append('0')
	elif platform == 'IOS':
		resultTags.append('1')
	
	if int(price) <= 18000:
		resultTags.append('2')
	elif int(price) >= 18001 and int(price) <= 40000:
		resultTags.append('3')
	elif int(price) >= 40001:
		resultTags.append('4')

	if float(diagonal) <= 5.5:
		resultTags.append('5')
	elif float(diagonal) >= 5.51 and float(diagonal) <= 6.59:
		resultTags.append('6')
	elif float(diagonal) >= 6.6:
		resultTags.append('7')

	if int(ram) <= 3:
		resultTags.append('8')
	elif int(ram) >= 4 and int(ram) <= 8:
		resultTags.append('9')
	elif int(ram) >= 9:
		resultTags.append('10')
	
	if int(rom) <= 32:
		resultTags.append('11')
	elif int(rom) >= 33 and int(rom) <= 255:
		resultTags.append('12')
	elif int(rom) >= 256:
		resultTags.append('13')

	if int(battery) <= 3000:
		resultTags.append('14')
	elif int(battery) >= 3001 and int(battery) <= 5500:
		resultTags.append('15')
	elif int(battery) >= 5501:
		resultTags.append('16')

	if (nfc):
		resultTags.append('17')

	if (sim):
		if sim == '2Sim':
			resultTags.append('18')

	if (five_g):
		resultTags.append('19')

	if (gps):
		resultTags.append('20')
	
	if (jack):
		resultTags.append('21')


	if int(processor) <= 2200:
		resultTags.append('22')
	elif int(processor) >= 2201 and int(processor) <= 3000:
		resultTags.append('23')
	elif int(processor) >= 3001:
		resultTags.append('24')

	if int(warranty) <= 9:
		resultTags.append('25')
	elif int(warranty) >= 10 and int(warranty) <= 20:
		resultTags.append('26')
	elif int(warranty) >= 21:
		resultTags.append('27')

	print(resultTags)
	return(resultTags)


def decodeTag(resultTags):
	resultDecode = []
	print(resultTags)
	if len(resultTags) !=0:
		if resultTags[0] == '0':
			resultDecode.append('Android')
		elif resultTags[0] == '1':
			resultDecode.append('iOS')
		resultTags.pop(0)
	
	if len(resultTags) != 0:
		if resultTags[0] == '2':
			resultDecode.append('смартфон до 18.000₽')
		elif resultTags[0] == '3':
			resultDecode.append('смартфон от 18.000₽ до 40.000₽')
		elif resultTags[0] == '4':
			resultDecode.append('Смартфон дороже 40.000₽')
		resultTags.pop(0)

	if len(resultTags) != 0:
		if resultTags[0] == '5':
			resultDecode.append('диагональ экрана меньше 5.5\"')
		elif resultTags[0] == '6':
			resultDecode.append('диагональ экрана от 5.5\" до 6.6\"')
		elif resultTags[0] == '7':
			resultDecode.append('диагональ экрана больше 6.6\"')
		resultTags.pop(0)

	if len(resultTags) != 0:
		if resultTags[0] == '8':
			resultDecode.append('оперативной памяти меньше 3 ГБ')
		elif resultTags[0] == '9':
			resultDecode.append('оперативной памяти от 4 ГБ до 8 ГБ')
		elif resultTags[0] == '10':
			resultDecode.append('оперативной памяти больше 9 ГБ')
		resultTags.pop(0)


	if len(resultTags) != 0:
		if resultTags[0] == '11':
			resultDecode.append('постоянной памяти меньше 32 ГБ')
		elif resultTags[0] == '12':
			resultDecode.append('постоянной памяти от 33 ГБ до 255 ГБ')
		elif resultTags[0] == '13':
			resultDecode.append('постоянной памяти больше 256 ГБ')
		resultTags.pop(0)

	if len(resultTags) != 0:
		if resultTags[0] == '14':
			resultDecode.append('батарея меньше 3000 мАч')
		elif resultTags[0] == '15':
			resultDecode.append('батарея от 3000 мАч до 5500 мАч')
		elif resultTags[0] == '16':
			resultDecode.append('батарея больше 5500 мАч')
		resultTags.pop(0)


	if len(resultTags) != 0:
		if resultTags[0] == '17':
			resultDecode.append('имеется NFC')
			resultTags.pop(0)
	if len(resultTags) != 0:
		if resultTags[0] == '18':
			resultDecode.append('поддержка 2 SIM')
			resultTags.pop(0)
	if len(resultTags) != 0:
		if resultTags[0] == '19':
			resultDecode.append('поддержка 5G')
			resultTags.pop(0)
	if len(resultTags) != 0:
		if resultTags[0] == '20':
			resultDecode.append('поддержка GPS')
			resultTags.pop(0)
	if len(resultTags) != 0:
		if resultTags[0] == '21':
			resultDecode.append('имеется разъем 3.5мм')
			resultTags.pop(0)

	if len(resultTags) != 0:
		if resultTags[0] == '22':
			resultDecode.append('процессор с частотой до 2200 ГГц')
		elif resultTags[0] == '23':
			resultDecode.append('процессор с частотой от 2200 ГГц до 3000 ГГц')
		elif resultTags[0] == '24':
			resultDecode.append('процессор с частотой от 3000 ГГц')
		resultTags.pop(0)

	if len(resultTags) != 0:
		if resultTags[0] == '25':
			resultDecode.append('гарантия до 9 мес.')
		elif resultTags[0] == '26':
			resultDecode.append('гарантия от 10 мес. до 20 мес.')
		elif resultTags[0] == '27':
			resultDecode.append('гарантия от 21 мес.')
		resultTags.pop(0)


	return(resultDecode)
