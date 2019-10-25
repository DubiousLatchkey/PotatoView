# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from serializers import PotatoSerializer
from potato.models import Potato
# Create your views here.

class potatoViewSet(viewsets.ModelViewSet):
	queryset = Potato.objects.all().order_by('name')
	serializer_class = PotatoSerializer

def listings(request):
	return HttpResponse("This is the potato listing")	
