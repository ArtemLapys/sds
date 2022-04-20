from sqlite3 import connect
from django.db import models
from django.http import JsonResponse
from django.urls import reverse

import json


class Post(models.Model):
	#1 элемент - для БД, 2 элемент - для админ панели
	mini_title = models.CharField(max_length=155, verbose_name="Заголовок на главной страницы" ) #заголовок для главной страницы 
	title = models.CharField(max_length=255, verbose_name="Заголовок статьи") #это крупный заголовок, который появляется в статье
	content = models.TextField(blank=True, verbose_name="Текст статьи")
	image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Изображение")
	time_create_post = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
	time_edit_post = models.DateTimeField(auto_now = True, verbose_name="Дата последнего редактирования")
	published = models.BooleanField(default=True,verbose_name="Опубликовано")
	
	def __str__(self):
		return self.title
		# return json.dumps(self.title)

	def get_absolute_url(self):
		return reverse('showPost', kwargs={'post_id': self.pk})
		# return reverse('post', kwargs={'post_id': self.pk})

	# Настройки админ панели
	class Meta:
		verbose_name = "пост" #изменение заголовка в админ панели
		verbose_name_plural = "Новости" #изменение множественного числа заголовка
		ordering = ['-time_create_post', 'title'] #сортировка идет сначала по полю создания, а потом, по полю title, если найдены одинаковые поля time_create