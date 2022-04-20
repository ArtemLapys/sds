from django.contrib import admin
# from jmespath import search

from .models import *



#Указываем в админ панели Новостей, что мы хотим видеть
class PostAdmin(admin.ModelAdmin):
	#Столбцы в панели новостей
	list_display = ('time_create_post', 'title', 'image', 'time_edit_post', 'published')
	#Поля клика, для перехода к след.статье
	list_display_links = ('time_create_post', 'title')
	#Поля для поиска в админке
	search_fields = ('title', 'contents')
	#Списки полей, который можно отредактировать прямо в таблице
	# list_editable = ('published',)
	#Список полей, для фильтрации статей в таблице
	list_filter = ('published', 'time_create_post', 'time_edit_post')

admin.site.register(Post, PostAdmin)