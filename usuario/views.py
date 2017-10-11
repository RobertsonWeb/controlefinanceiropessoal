# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from .models import Usuario

class UsuarioListView(LoginRequiredMixin, ListView):
	model = Usuario


class UsuarioCreateView(LoginRequiredMixin, CreateView):
	model = Usuario
	fields = ['tipo', 'nome', 'email', 'password', 'is_active']
	success_url = 'usuario_list'


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
	model = Usuario
	fields = ['tipo', 'nome', 'email', 'is_active']
	success_url = 'usuario_list'


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
	model = Usuario
	success_url = 'usuario_list'