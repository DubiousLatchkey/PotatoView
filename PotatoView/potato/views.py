# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from serializers import PotatoSerializer
from serializers import ShortPotatoSerializer
from potato.models import Potato
from django.http import Http404
# Create your views here.

class PotatoList(APIView):

	def get(self, request, format=None):
		potatoes = Potato.objects.all()
		serializer = ShortPotatoSerializer(potatoes, many = True)
		return Response(serializer.data)

class PotatoDetail(APIView):
	def get_object(self, id):
	        try:
		 	return Potato.objects.get(id=id)
		except Potato.DoesNotExist:
			raise Http404
	def get(self, request, id, format=None):
		potato = self.get_object(id)
		serializer = PotatoSerializer(potato)
		return Response(serializer.data)
