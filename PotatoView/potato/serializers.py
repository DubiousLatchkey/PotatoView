from potato.models import Potato
from rest_framework import serializers
from django.db import models

class PotatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = models.Model
	    fields = ['name', 'description', 'species', 'varieties', 'colors', 'image_url']


