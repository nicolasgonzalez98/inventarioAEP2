import django_filters
from django.db import models
from django import forms

from .models import *


class HardwareFilter(django_filters.FilterSet):

    tipo = django_filters.ModelChoiceFilter(
        queryset=Tipo.objects.all(),
        empty_label="Cualquier tipo",
        label="Tipo",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    
    marca = django_filters.ModelChoiceFilter(
        queryset=Marca.objects.all(),
        empty_label="Cualquier marca",
        label="Marca",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    
    modelo = django_filters.ModelChoiceFilter(
        queryset=Modelo.objects.all(),
        empty_label="Cualquier modelo",
        label="Modelo",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    
    ubicacion = django_filters.ModelChoiceFilter(
        queryset = Ubicacion.objects.all(),
        empty_label="Cualquier ubicación",
        label="Ubicación",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    estado = django_filters.ModelChoiceFilter(
        queryset = Estado.objects.all(),
        empty_label='Cualquier estado',
        label="Estado",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Hardware
        fields = ['nro_de_serie', 'tipo', 'marca', 'modelo', 'ubicacion']
        filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                     'widget': forms.TextInput(attrs={'class': 'form-control'})
                 },
             }
        }

class AsignacionFilter(django_filters.FilterSet):
    

    class Meta:
        model = Asignacion
        fields = {
            'usuario':  ['icontains'], 
            'nro_ticket': ["exact"], 
            'hardware__nro_de_serie': ['icontains']
        }

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'widget': forms.TextInput(attrs={'class': 'form-control'})
                },
            }
        }
