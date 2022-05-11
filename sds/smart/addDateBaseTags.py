# import sys
# sys.path.append("../smart/")


from .models import phones, Tagis, TagsPhones

#Добавить тег только 1 модели
def addTags(obj):
	if (TagsPhones.objects.filter(phone_id=obj.id).exists()):
		TagsPhones.objects.filter(phone_id=obj.id).delete()
	if obj.platform == 'Android':
		tempPlatform = TagsPhones(phone_id = str(obj.id), tag_id= '0')
	elif obj.platform == 'IOS':
		tempPlatform = TagsPhones(phone_id=str(obj.id), tag_id='1')
	tempPlatform.save()

	if obj.price <= 18000:
		tempPrice = TagsPhones(phone_id=str(obj.id), tag_id='2')
	elif obj.price >= 18001 and obj.price <= 40000:
		tempPrice = TagsPhones(phone_id=str(obj.id), tag_id='3')
	elif obj.price >= 40001:
		tempPrice = TagsPhones(phone_id=str(obj.id), tag_id='4')
	tempPrice.save()

	if obj.diagonal <= 5.5:
		tempDiagonal = TagsPhones(phone_id=str(obj.id), tag_id='5')
	elif obj.diagonal >= 5.51 and obj.diagonal <= 6.59:
		tempDiagonal = TagsPhones(phone_id=str(obj.id), tag_id='6')
	elif obj.diagonal >= 6.6:
		tempDiagonal = TagsPhones(phone_id=str(obj.id), tag_id='7')
	tempDiagonal.save()

	if obj.ram <= 3:
		tempRam = TagsPhones(phone_id=str(obj.id), tag_id='8')
	elif obj.ram >= 4 and obj.ram <= 8:
		tempRam = TagsPhones(phone_id=str(obj.id), tag_id='9')
	elif obj.ram >= 9:
		tempRam = TagsPhones(phone_id=str(obj.id), tag_id='10')
	tempRam.save()


	if obj.rom <= 32:
		tempRom = TagsPhones(phone_id=str(obj.id), tag_id='11')
	elif obj.rom >= 33 and obj.rom <= 255:
		tempRom = TagsPhones(phone_id=str(obj.id), tag_id='12')
	elif obj.rom >= 256:
		tempRom = TagsPhones(phone_id=str(obj.id), tag_id='13')
	tempRom.save()


	if obj.battery <= 3000:
		tempBattery = TagsPhones(phone_id=str(obj.id), tag_id='14')
	elif obj.battery >= 3001 and obj.battery <= 5500:
		tempBattery = TagsPhones(phone_id=str(obj.id), tag_id='15')
	elif obj.battery >= 5501:
		tempBattery = TagsPhones(phone_id=str(obj.id), tag_id='16')
	tempBattery.save()


	if obj.nfc == 1:
		tempNfc = TagsPhones(phone_id=str(obj.id), tag_id='17')
		tempNfc.save()
	if obj.sim == 2:
		tempSim = TagsPhones(phone_id=str(obj.id), tag_id='18')
		tempSim.save()
	if obj.five_g == 1:
		tempFive_g = TagsPhones(phone_id=str(obj.id), tag_id='19')
		tempFive_g.save()
	if obj.gps == 1:
		tempGps = TagsPhones(phone_id=str(obj.id), tag_id='20')
		tempGps.save()
	if obj.jack == 1:
		tempJack = TagsPhones(phone_id=str(obj.id), tag_id='21')
		tempJack.save()

	if obj.processor_frequency <= 2200:
		tempProcessor = TagsPhones(phone_id=str(obj.id), tag_id='22') 
	elif obj.processor_frequency >= 2201 and obj.processor_frequency <= 3000:
		tempProcessor = TagsPhones(phone_id=str(obj.id), tag_id='23')
	elif obj.processor_frequency >= 3001:
		tempProcessor = TagsPhones(phone_id=str(obj.id), tag_id='24')
	tempProcessor.save()

	if obj.warranty <= 9:
		tempWarranty = TagsPhones(phone_id=str(obj.id), tag_id='25')
	elif obj.warranty >= 10 and obj.warranty <= 20:
		tempWarranty = TagsPhones(phone_id=str(obj.id), tag_id='26')
	elif obj.warranty >= 21:
		tempWarranty = TagsPhones(phone_id=str(obj.id), tag_id='27')
	tempWarranty.save()
	print("For " +obj.title+" tags added.")





#добавить теги всем моделям
def oneAddTags():
	for obj in phones.objects.all():
		print(obj.id)
		if obj.platform == 'Android':
			tempPlatform = TagsPhones(phone_id=str(obj.id), tag_id='0')
		elif obj.platform == 'IOS':
			tempPlatform = TagsPhones(phone_id=str(obj.id), tag_id='1')
			print("platform")
		tempPlatform.save()

		if obj.price <= 18000:
			tempPrice = TagsPhones(phone_id=str(obj.id), tag_id='2')
		elif obj.price >= 18001 and obj.price <= 40000:
			tempPrice = TagsPhones(phone_id=str(obj.id), tag_id='3')
		elif obj.price >= 40001:
			tempPrice = TagsPhones(phone_id=str(obj.id), tag_id='4')
		tempPrice.save()

		if obj.diagonal <= 5.5:
			tempDiagonal = TagsPhones(phone_id=str(obj.id), tag_id='5')
		elif obj.diagonal >= 5.51 and obj.diagonal <= 6.59:
			tempDiagonal = TagsPhones(phone_id=str(obj.id), tag_id='6')
		elif obj.diagonal >= 6.6:
			tempDiagonal = TagsPhones(phone_id=str(obj.id), tag_id='7')
		tempDiagonal.save()

		if obj.ram <= 3:
			tempRam = TagsPhones(phone_id=str(obj.id), tag_id='8')
		elif obj.ram >= 4 and obj.ram <= 8:
			tempRam = TagsPhones(phone_id=str(obj.id), tag_id='9')
		elif obj.ram >= 9:
			tempRam = TagsPhones(phone_id=str(obj.id), tag_id='10')
		tempRam.save()

		if obj.rom <= 32:
			tempRom = TagsPhones(phone_id=str(obj.id), tag_id='11')
		elif obj.rom >= 33 and obj.rom <= 255:
			tempRom = TagsPhones(phone_id=str(obj.id), tag_id='12')
		elif obj.rom >= 256:
			tempRom = TagsPhones(phone_id=str(obj.id), tag_id='13')
		tempRom.save()

		if obj.battery <= 3000:
			tempBattery = TagsPhones(phone_id=str(obj.id), tag_id='14')
		elif obj.battery >= 3001 and obj.battery <= 5500:
			tempBattery = TagsPhones(phone_id=str(obj.id), tag_id='15')
		elif obj.battery >= 5501:
			tempBattery = TagsPhones(phone_id=str(obj.id), tag_id='16')
		tempBattery.save()

		if obj.nfc == 1:
			tempNfc = TagsPhones(phone_id=str(obj.id), tag_id='17')
			tempNfc.save()
		if obj.sim == 2:
			tempSim = TagsPhones(phone_id=str(obj.id), tag_id='18')
			tempSim.save()
		if obj.five_g == 1:
			tempFive_g = TagsPhones(phone_id=str(obj.id), tag_id='19')
			tempFive_g.save()
		if obj.gps == 1:
			tempGps = TagsPhones(phone_id=str(obj.id), tag_id='20')
			tempGps.save()
		if obj.jack == 1:
			tempJack = TagsPhones(phone_id=str(obj.id), tag_id='21')
			tempJack.save()

		if obj.processor_frequency <= 2200:
			tempProcessor = TagsPhones(phone_id=str(obj.id), tag_id='22')
		elif obj.processor_frequency >= 2201 and obj.processor_frequency <= 3000:
			tempProcessor = TagsPhones(phone_id=str(obj.id), tag_id='23')
		elif obj.processor_frequency >= 3001:
			tempProcessor = TagsPhones(phone_id=str(obj.id), tag_id='24')
		tempProcessor.save()

		if obj.warranty <= 9:
			tempWarranty = TagsPhones(phone_id=str(obj.id), tag_id='25')
		elif obj.warranty >= 10 and obj.warranty <= 20:
			tempWarranty = TagsPhones(phone_id=str(obj.id), tag_id='26')
		elif obj.warranty >= 21:
			tempWarranty = TagsPhones(phone_id=str(obj.id), tag_id='27')
		tempWarranty.save()
		print(obj.title + " --Tag add--")







