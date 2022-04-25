from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core import serializers

from .forms import *
# from django.http import JsonResponse

# from django.views.generic import ListView
# from http.client import HTTPResponse

from .models import Post

import json

menuHeader = [{'title': "Новости", 'url_name': 'news'},
              {'title': "Выбор смартфона", 'url_name': 'sds'},
              {'title': "Маркет-Плейсы", 'url_name': 'marketplace'},
              {'title': "Контакты", 'url_name': 'contacts'},
              {'title': "⚙", 'url_name': 'settings'}]

menuFooter = [{'title': "Правообладатель", 'url_name': 'copyright'},
              {'title': "Вакансии", 'url_name': 'jobs'},
              {'title': "Настройки", 'url_name': 'settings'},
              {'title': "English Version", 'url_name': 'en'}]


def index(request):  # link HttpRequest
    posts = Post.objects.all()
    dataForPage = {
        'title': 'SDS News',
        'posts': posts,
        'menuHeader': menuHeader,
        'menuFooter': menuFooter
    }
    return render(request, 'news/index.html', context=dataForPage)


def sds(request):
    return HttpResponse("Sds")


def marketplace(request):
    return HttpResponse("marketplace")


def contacts(request):  # link HttpRequest
    return render(request, 'news/contacts.html', {'menuFooter': menuFooter, 'title': 'SDS Contacts'})


def settingsPage(request):
    return HttpResponse("settings")


def copyright(request):
    return HttpResponse("copyright")


def jobs(request):
    return HttpResponse("jobs")


def en(request):
    return HttpResponse("en")


def showPost(request, post_id, post_slug):
    post = get_object_or_404(Post, pk=post_id, slug=post_slug)

    dataForPage = {
        'post': post,
        'menuHeader': menuHeader,
        'menuFooter': menuFooter,
        'title': post.title,

    }

    return render(request, 'news/post.html', context=dataForPage)


def addPost(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          return redirect('main')

    else:
        form = AddPostForm()

    dataForPage = {
		'title': 'Добавить пост',
		'menuHeader': menuHeader,
		'menuFooter': menuFooter,
		'form': form,
	}
    return render(request, 'news/addPost.html', context=dataForPage)


# Debug Information Pages
def json(request):
    qs = Post.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')

    # data = list(Post.Objects.values())
    # return JsonResponse(data, safe=False)
