# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Potato(models.Model):
	name = models.CharField(max_length=50, default='9gag')
	description = models.CharField(max_length=1000, default='Not Reddit')
	species = models.CharField(max_length=50, default='netizen')
	variety = models.CharField(max_length=50, default='normie')
	colors = models.CharField(max_length=200, default='white and black')
	image_url = models.CharField(max_length=200, default='9gag.com')

