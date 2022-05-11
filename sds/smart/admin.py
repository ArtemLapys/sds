from socket import timeout
from django.contrib import admin
from django.utils.safestring import mark_safe

from smart.addDateBaseTags import addTags, oneAddTags

from .models import *



class PhonesAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'platform',
                 'price', 'sim', 'image')
	
	list_display_links = ('id', 'title', 'platform', 'price', 'sim')

	search_fields = ('title', 'platform', 'price')

	# list_filter = ('id', 'title')

	save_on_top = True

	fields = ('title', 'image', 'get_image', 'platform', 'price',
           'diagonal', 'ram', 'rom', 'processor_frequency', 'battery', 'warranty', 'sim', 'nfc', 'five_g', 'gps', 'jack')

	readonly_fields = ('get_image', 'id')

	    # получение миниатюры изображения
	def get_image(self, object):
		if object.image:
			return mark_safe(f"<img src='{object.image.url}' width=200")

    # изменение заголовка у функции
	get_image.short_description = "Миниатюра изорабжения"


	def save_model(self, request, obj, form, change):
		
		super().save_model(request, obj, form, change)
		# oneAddTags() #Добавить всем уже имеющимся устройствам теги
		addTags(obj) #Добавить теги к объекту

class TagisAdmin(admin.ModelAdmin):
	list_display = ('id', 'title_tag', 'filter')

	list_display_links = ('id', 'title_tag', 'filter')

	search_fields = ('id', 'title_tag', 'filter')

	fields = ('id', 'title_tag', 'filter')

	readonly_fields = ['id']


class TagsPhonesAdmin(admin.ModelAdmin):
	list_display = ('id', 'phone', 'tag')

	list_display_links = ('id', 'phone', 'tag')

	search_fields = ('id', 'phone', 'tag')

	fields = ('id', 'phone', 'tag')

	readonly_fields = ['id']


# Register your models here.
admin.site.register(phones, PhonesAdmin)
admin.site.register(Tagis, TagisAdmin)
admin.site.register(TagsPhones, TagsPhonesAdmin)