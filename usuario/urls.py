from django.conf.urls import url

from .views import UsuarioListView, UsuarioCreateView
from .views import UsuarioUpdateView, UsuarioDeleteView


urlpatterns = [
	url(r'list/$', UsuarioListView.as_view(), name='usuario_list'),
	url(r'cad/$', UsuarioCreateView.as_view(), name='usuario_create'),
	url(r'(?P<pk>\d+)/$', UsuarioUpdateView.as_view(), name='usuario_update'),
	url(r'(?P<pk>\d+)/delete/$', UsuarioDeleteView.as_view(), name='usuario_delete'),
]