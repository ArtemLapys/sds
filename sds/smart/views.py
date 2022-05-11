from django.http import HttpResponse
from django.shortcuts import render
from requests import request

from news.views import *
from .models import phones, TagsPhones
from statistics import mean
from django.db.models import Avg, Max, Min, Q
from .roundObj import RoundObjects
from .addTagsUserRequest import addTagsForRequestUser, decodeTag
from django.db.models.aggregates import Count

def sds(request):
	priceAll = RoundObjects(phones.objects.all().aggregate(
		Min('price'), Max('price'), Avg('price')),0)
	diagonalAll = RoundObjects(phones.objects.all().aggregate(
		Min('diagonal'), Max('diagonal'), Avg('diagonal')), 1)
	ramAll = RoundObjects(phones.objects.all().aggregate(
		Min('ram'), Max('ram'), Avg('ram')), 0)
	romAll=RoundObjects(phones.objects.all().aggregate(
		Min('rom'), Max('rom'), Avg('rom')), 0)
	batteryAll=RoundObjects(phones.objects.all().aggregate(
		Min('battery'), Max('battery'), Avg('battery')), 0)
	processorAll=RoundObjects(phones.objects.all().aggregate(
		Min('processor_frequency'), Max('processor_frequency'), Avg('processor_frequency')), 0)
	warrantyAll = RoundObjects(phones.objects.all().aggregate(
		Min('warranty'), Max('warranty'), Avg('warranty')), 0)
	
      
	dataForPage = {
        'priceAll': priceAll,
        'diagonalAll': diagonalAll,
        'ramAll': ramAll,
        'romAll': romAll,
        'batteryAll':batteryAll,
        'processorAll':processorAll,
        'warrantyAll': warrantyAll,
        'menuHeader': menuHeader,
        'menuFooter': menuFooter,
        'title': "SDS Smart",

    }


	return render(request, 'smart/sds.html', context=dataForPage)


def resultSds(request):
	if (request.GET):
		resultTags = addTagsForRequestUser(request.GET)
		
		saveResultTags = resultTags

		smart = phones.objects.filter(id__in=[obj.get('phone_id') for obj in TagsPhones.objects.filter(tag_id__in=resultTags).values(	'phone_id').annotate(count_tag_id=Count('tag_id', distinct=True)).filter(count_tag_id=len(resultTags))])

		while len(smart) == 0:
			resultTags = resultTags[:-1]
			smart = phones.objects.filter(id__in=[obj.get('phone_id') for obj in TagsPhones.objects.filter(tag_id__in=resultTags).values(
				'phone_id').annotate(count_tag_id=Count('tag_id', distinct=True)).filter(count_tag_id=len(resultTags))])


		smartResultId=[]
		for i in range(len(smart)):
			smartResultId.append(smart[int(i)].pk)

		
		
		smartDop = phones.objects.filter(id__in=[obj.get('phone_id') for obj in TagsPhones.objects.filter(tag_id__in=resultTags).values('phone_id').annotate(
			count_tag_id=Count('tag_id', distinct=True)).filter(Q(count_tag_id=len(resultTags)) | Q(count_tag_id=5))]).exclude(id__in=smartResultId)

		if len(smartDop) == 0:
			smartDop = False

		tagsEdit = None
		if len(saveResultTags) != len(resultTags):
			tagsEdit = True

		smartAll = False
		resultTagDecode = ', '.join(decodeTag(resultTags))
	else:
		tagsEdit = False
		smart = False
		resultTagDecode = False
		smartDop = False
		smartAll = phones.objects.all()


	

	dataForPage = {
            'tags': resultTagDecode,
            'smarts': smart,
			'tagsEdit': tagsEdit,
			'smartsAll': smartAll,
			'smartsDop': smartDop,
            'menuHeader': menuHeader,
            'menuFooter': menuFooter,
            'title': "SDS Smart",

        }

	# print(request.GET)

	return render(request, 'smart/resultSds.html', context=dataForPage)

def resultAll(request):
	smart = phones.objects.all()  # [:5]
	dataForPage = {
            'smarts': smart,
            'menuHeader': menuHeader,
            'menuFooter': menuFooter,
            'title': "SDS Smart",

        }

	return render(request, 'smart/resultSds.html', context=dataForPage)



def marketplace(request):
    dataForPage = {

        'menuHeader': menuHeader,
        'menuFooter': menuFooter,
        'title': "SDS Marketplace",

    }

    return render(request, 'news/post.html', context=dataForPage)
