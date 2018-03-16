# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from utils.decorators import LoginRequiredMixin

from .models import Conta


class ContaListView(LoginRequiredMixin, ListView):
	model = Conta


class ContaCreateView(LoginRequiredMixin, CreateView):
	model = Conta
	fields = ['descricao']
	success_url = 'conta_list'


class ContaUpdateView(LoginRequiredMixin, UpdateView):
	model = Conta
	fields = ['descricao']
	success_url = 'conta_list'