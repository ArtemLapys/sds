from django.urls import path
from django.views.generic.base import RedirectView



from .views import *
from sds import settings
from django.conf.urls.static import static

urlpatterns = [
    #icon
    path('favicon.ico', RedirectView.as_view(url="../static/news/images/favicon.ico")),

    # Urls for pages
    path('', mainPage, name='main'),
    path('', mainPage, name='news'),
    path('sds/', sds, name='sds'),
    path('marketplace/', marketplace, name='marketplace'),
    path('contacts/', contacts, name='contacts'),
    path('settings/', settingsPage, name='settings'),

    path('copyright/', copyright, name='copyright'),
    path('jobs/', jobs, name='jobs'),
    path('en/', en, name='en'),

    # urls for post
    path('post/<int:post_id>-<slug:post_slug>/',
         showPost, name='showPost'),


    # Debug Information
    path('api/json/<int:count>', ApiJson, name='json'),
    path('api/json-post/<int:post_id>', postApi, name='postJson'),

    # AddPost
    path('add-post', AddPost.as_view(), name='addPost'),


]

# В режиме отладки нужно обязательно указать строки, чтобы загружались медиа данные
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



