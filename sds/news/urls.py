from django.urls import path

from .views import *
from sds import settings
from django.conf.urls.static import static

urlpatterns = [
	# Urls for pages
	path('', index, name= 'main'),
	path('news/', index, name= 'news'),
	path('sds/', sds, name = 'sds'),
	path('marketplace/', marketplace, name = 'marketplace'),
	path('contacts/', contacts, name = 'contacts'),
	path('settings/', settingsPage, name = 'settings'),

	path('copyright/', copyright, name = 'copyright'),
	path('jobs/', jobs, name = 'jobs'),
	path('en/', en, name = 'en'),

	#urls for post
	path('post/<int:post_id>/', showPost, name='showPost'),


	#Debug Information
	path('json', json, name= 'json')	

]

# В режиме отладки нужно обязательно указать строки, чтобы загружались медиа данные 
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)