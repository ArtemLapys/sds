# from xml.etree.ElementInclude import url, include
from django.urls import path, include

from .views import *

urlpatterns = [

	path('', sds, name="smartSDS"),
	path('result', resultSds, name="resultSDS"),
	path('result-all', resultAll, name="resultAll"),


]

