from faulthandler import disable
from django.contrib import admin
# from jmespath import search
from django.utils.safestring import mark_safe

from .models import *


# Указываем в админ панели Новостей, что мы хотим видеть
class PostAdmin(admin.ModelAdmin):
    # Столбцы в панели новостей
    list_display = ('time_create_post', 'title', 'image',
                    'time_edit_post', 'published')

    # Поля клика, для перехода к след.статье
    list_display_links = ('time_create_post', 'title')

    # Поля для поиска в админке
    search_fields = ('title', 'contents')

    # Списки полей, который можно отредактировать прямо в таблице
    # list_editable = ('published',)

    # Список полей, для фильтрации статей в таблице
    list_filter = ('published', 'time_create_post', 'time_edit_post')

    # создание автоматического заголовка на основе title
    prepopulated_fields = {"slug": ("title",)}

    # поля, которые нужно показать(если поле не указано в readonly_fields - значит его можно редактировать)
    fields = ('title', 'slug', 'content', 'image', 'get_image',
              'published', 'time_create_post', 'time_edit_post')

    readonly_fields = ('time_create_post', 'time_edit_post',
                       'get_image')
    


    # получение миниатюры изображения
    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=200")

    # изменение заголовка у функции
    get_image.short_description = "Миниатюра изорабжения"

    # Панель с кнопками "Удалить/сохранить" будет появляться сверху и снизу
    save_on_top = True


admin.site.register(Post, PostAdmin)
