from django.apps import AppConfig

#конфигурация всего приложения
class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Компоненты SDS' #в админ панели изменить название группы компонентов общего приложения SDS
