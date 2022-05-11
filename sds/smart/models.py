from enum import unique
from django.db import models
from django.db.models.signals import post_save

# from smart.addDateBaseTags import addTags

class phones(models.Model):

	platforms = [
		("Android", 'Android'),
		("IOS", 'IOS'),
	]

	simChoice = [
		(1, '1 SIM'),
		(2, '2 SIM')
	]

	title = models.CharField(max_length=255, verbose_name="Название смартфона")
	image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Изображение")
	platform = models.CharField(
		max_length=100, verbose_name="Платформа", choices=platforms, default="Android")
	price = models.IntegerField(verbose_name="Цена (₽)")
	diagonal = models.FloatField(verbose_name="Диагональ (\")")
	ram = models.IntegerField(verbose_name="Оперативная память (ГБ)")
	rom = models.IntegerField(verbose_name="Постоянная память (ГБ)")
	battery = models.IntegerField(verbose_name="Емкость батареи (мAч)")
	nfc = models.BooleanField(default=True, verbose_name="NFC")
	sim = models.IntegerField(verbose_name="Количество SIM", choices=simChoice, default = 1)
	five_g = models.BooleanField(default=False, verbose_name="5G интернет")
	gps = models.BooleanField(default=True, verbose_name="GPS")
	jack = models.BooleanField(default=True, verbose_name="Разъем 3.5мм")
	processor_frequency = models.IntegerField(
		verbose_name="Частота процессора (МГц)")
	warranty = models.IntegerField(verbose_name="Гарантия (мес.)")

	def __str__(self):
		return self.title
		

	
	class Meta:
		verbose_name = "смартфон"  # изменение заголовка в админ панели
		verbose_name_plural = "Смартфоны"  # изменение множественного числа заголовка
		# сортировка идет сначала по полю создания, а потом, по полю title, если найдены одинаковые поля time_create
		ordering = ['id']

class Tagis(models.Model):
	title_tag = models.CharField(max_length=255, verbose_name="Название тега")
	filter = models.CharField(max_length=255, verbose_name="Поле фильтрации")

	def __str__(self):
		return self.title_tag

	class Meta:
		verbose_name = "тег смартфона"  # изменение заголовка в админ панели
		verbose_name_plural = "Теги смартфонов"  # изменение множественного числа заголовка
	# сортировка идет сначала по полю создания, а потом, по полю title, если найдены одинаковые поля time_create
		ordering = ['id']

class TagsPhones(models.Model):
	phone = models.ForeignKey(phones, on_delete=models.CASCADE)
	tag = models.ForeignKey('Tagis', on_delete=models.CASCADE)


	class Meta:
		verbose_name = "связь тега и смартфона"  # изменение заголовка в админ панели
		# изменение множественного числа заголовка
		verbose_name_plural = "Связь тегов и смартфонов"
	# сортировка идет сначала по полю создания, а потом, по полю title, если найдены одинаковые поля time_create
		ordering = ['id']

		unique_together = (('phone', 'tag'))

# def article_post_save(*args, instance, created, **kwargs):
# 	print('post_save')
# 	if (created):
# 		obj = phones.objects.get(title=str(instance))
# 		addTags(obj)


# post_save.connect(article_post_save, sender=phones)
