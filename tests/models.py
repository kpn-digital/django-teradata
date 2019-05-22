# -*- coding: utf-8 -*-

from django.db.models import Model


class SampleModel(Model):
    class Meta:
        app_label = 'sample_model'


class OrderedSampleModel(SampleModel):
    class Meta:
        ordering = ['id']
        app_label = 'sample_model'
