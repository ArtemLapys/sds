from django.apps import AppConfig


class SmartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smart'
    verbose_name = 'Компоненты смартфонов' #в админ панели изменить название группы компонентов общего приложения SDS