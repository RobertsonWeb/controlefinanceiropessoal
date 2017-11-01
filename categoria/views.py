# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from utils.decorators import LoginRequiredMixin

from .models import Categoria


class CategoriaListView(LoginRequiredMixin, ListView):
	model = Categoria


class CategoriaCreateView(LoginRequiredMixin, CreateView):
	model = Categoria
	fields = ['tipo', 'descricao', 'is_active']
	success_url = 'categoria_list'


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
	model = Categoria
	fields = ['descricao', 'tipo', 'is_active']
	success_url = 'categoria_list'