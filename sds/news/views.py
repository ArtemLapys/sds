from asyncio.windows_events import NULL
from ctypes import sizeof
from re import template
from tkinter.tix import Tree
from django.shortcuts import get_object_or_404, redirect, render
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
# from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from numpy import array


from io import BytesIO


from requests import request


from .forms import *
# from django.http import JsonResponse

# from django.views.generic import ListView
# from http.client import HTTPResponse

from .models import Post

# import ormsgpack
import msgpack
# import msgpack_serializer.serializer


import umsgpack
from nameko_django.serializer import dumps, loads


menuHeader = [{'title': "Новости", 'url_name': 'news'},
              {'title': "Выбор смартфона", 'url_name': 'sds'},
              {'title': "Маркет-Плейсы", 'url_name': 'marketplace'},
              {'title': "Контакты", 'url_name': 'contacts'},
              {'title': "⚙", 'url_name': 'settings'}]

menuFooter = [{'title': "Правообладатель", 'url_name': 'copyright'},
              {'title': "Вакансии", 'url_name': 'jobs'},
              {'title': "Настройки", 'url_name': 'settings'},
              {'title': "English Version", 'url_name': 'en'}]




def mainPage(request):  # link HttpRequest
    dataForPage = {
        'title': 'SDS News',
        'menuHeader': menuHeader,
        'menuFooter': menuFooter
    }
    return render(request, 'news/index.html', context=dataForPage)


# def sds(request):
#     dataForPage = {

#     'menuHeader': menuHeader,
#     'menuFooter': menuFooter,
#     'title': "sds",

#     }

#     return render(request, 'news/post.html', context=dataForPage)   


# def marketplace(request):
#     return HttpResponse("marketplace")


def contacts(request):  # link HttpRequest
    return render(request, 'news/contacts.html', {'menuFooter': menuFooter, 'title': 'SDS Contacts'})


def settingsPage(request):
    dataForPage = {
        'title': 'SDS Settings',
        'menuHeader': menuHeader,
        'menuFooter': menuFooter
    }
    return render(request, 'news/settings.html', context=dataForPage)




def redirect(request):
	if (len(request.GET)==0):
		buttonEco = None
		response = HttpResponseRedirect(redirect_to='/')
		response.delete_cookie("eco", buttonEco)
		return response
	elif (request.GET):
		buttonEco = request.GET["buttonEco"]
		if buttonEco == "true":
			response = HttpResponseRedirect(redirect_to='/')
			response.set_cookie("eco", request.GET["buttonEco"])
			print(request.GET["buttonEco"])
			return response
		else:
			return HttpResponseRedirect(redirect_to='/')
	else:
		return HttpResponseRedirect(redirect_to='/')

def copyright(request):
    return HttpResponse("copyright")


def jobs(request):
    dataForPage = {

    'menuHeader': menuHeader,
    'menuFooter': menuFooter,
    'title': "jobs",

    }

    return render(request, 'news/post.html', context=dataForPage)   


def en(request):
    return HttpResponse("en")


def showPost(request, post_id, post_slug):
    # post = get_object_or_404(Post, pk=post_id, slug=post_slug)
    post = Post.objects.get(pk=post_id)
    post_json = serializers.serialize('json', [post])

    dataForPage = {
        'post': post_json,
        'menuHeader': menuHeader,
        'menuFooter': menuFooter,
        'title': post.title,

    }

    return render(request, 'news/post.html', context=dataForPage)


def postApi(request, post_id):
    post = Post.objects.get(pk=post_id)
    post_json = serializers.serialize('json', [post])
    return HttpResponse(post_json, content_type='application/json')



class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'news/addPost.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # передать все именованые параметры
        context['title'] = 'Добавить пост в раздел "Новости"'# статический
        context['menuHeader'] = menuHeader  # динамическийы
        context['menuFooter'] = menuFooter
        return context


def ApiJson(request, count):
    qs = Post.objects.filter(published=True)[count: count+5]
    qs_json = serializers.serialize('json', qs)
    print(qs_json.__sizeof__())
    return HttpResponse(qs_json, content_type='application/json')


def ApiMsgpack(request, count):
    qs = Post.objects.filter(published=True)[count: count+5]
    qs_json = serializers.serialize('json', qs)
    data = msgpack.packb(qs_json)
    # print(data)

    # data = msgpack.unpackb(data)
    # print(data.__sizeof__())
    # data = dumps(qs)
    # data = msgpack.unpackb(data)
    # print(data)
    # print(data.__sizeof__())
    # msgpack_serializer = serializers.get_serializer("msgpack")()
    # data = msgpack_serializer.serialize(qs)
    # qs_msgpack = msgpack.packb(qs, use_bin_type=True)
    # qs_unmsgpack = msgpack.unpackb(qs_msgpack, use_list=False, raw=False)
    # qs_unpack = msgpack.unpack(qs_msgpack, use_list=False, raw=False)
    # qs_unpack
    # data = int(data)
    data = data.hex()
    # print(type(data))
    # print(data.__sizeof__(q``))
    return HttpResponse((data))
    # response = HttpResponse(data)


    # response['Content-Type'] = 'text/csv'
    # return response

def PostApiMsg(request, post_id):
    post = Post.objects.get(pk=post_id)
    post_json = serializers.serialize('json', [post])
    print(post_json.__sizeof__())
    data = msgpack.packb(post_json)
    data = data.hex()
    print(data.__sizeof__())
    return HttpResponse(data)


# def setcookie(request):
#     set_cookie('dataflair', 'Hello this is your Cookies', max_age=None)
#     return html

# def showcookie(request):
#     show = request.COOKIES['dataflair']
#     html = "<center> New Page <br>{0}</center>".format(show)
#     return HttpResponse(html)




        
# # Debug Information Pages
# def json(request):
#     qs = Post.objects.last()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')

# def jsonPost(requst):
#     qs = 
    # data = list(Post.Objects.values())
    # return JsonResponse(data, safe=False)



#Классы по Django views
# class MainPage(ListView):
#     # model = Post.objects.all()[:2]
#     template_name = 'news/index.html'
#     context_object_name = 'posts'  # для того, чтобы работала внутренняя переменная posts

#     # функция для передачи динамического списка
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)  # передать все именованые параметры
#         context['title'] = 'SDS News'  # статический
#         context['menuHeader'] = menuHeader  # динамическийы
#         context['menuFooter'] = menuFooter
#         return context

#     def get_queryset(self):  # функция для отправки данных, при условии поля published==true
#         return Post.objects.filter(published=True)


# class ShowPost(DetailView):
#     model = Post
#     template_name = 'news/post.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'

#     # функция для передачи динамического списка

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)  # передать все именованые параметры
#         context['title'] = context['post']  # статический
#         context['menuHeader'] = menuHeader  # динамическийы
#         context['menuFooter'] = menuFooter
#         return context


# def addPost(request):

#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#           form.save()
#           return redirect('main')

#     else:
#         form = AddPostForm()

#     dataForPage = {
# 		'title': 'Добавить пост',
# 		'menuHeader': menuHeader,
# 		'menuFooter': menuFooter,
# 		'form': form,
# 	}
#     return render(request, 'news/addPost.html', context=dataForPage)


