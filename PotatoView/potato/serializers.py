from potato.models import Potato
from rest_framework import serializers
from django.db import models

class PotatoSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True) 
	name = serializers.CharField(required=False, allow_blank=True, max_length=50)
	description = serializers.CharField(required=False, allow_blank=True, max_length=1000)
	species = serializers.CharField(required=False, allow_blank=True, max_length=50)
	variety = serializers.CharField(required=False, allow_blank=True, max_length=50)
	colors = serializers.CharField(required=False, allow_blank=True, max_length=200)
	image_url = serializers.CharField(required=False, allow_blank=True, max_length=200)
	
	def create(self, validated_data):
		return Potato.objects.create(**validated_data)
	def update(self, instance, validated_data):
		Potato.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.species = validated_data.get('species', instance.species)
		instance.variety = validated_data.get('variety', instance.variety)
		instance.colors = validated_data.get('colors', instance.colors)
		image_url = validated_data.get('image_url', instance.image_url)
		instance.save()
		return instance

class ShortPotatoSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True) 
	name = serializers.CharField(required=False, allow_blank=True, max_length=50)
	species = serializers.CharField(required=False, allow_blank=True, max_length=50)
	variety = serializers.CharField(required=False, allow_blank=True, max_length=50)


