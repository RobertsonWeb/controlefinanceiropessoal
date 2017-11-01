from django.conf.urls import url

from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView


urlpatterns = [
	url(r'list/$', CategoriaListView.as_view(), name='categoria_list'),
	url(r'cad/$', CategoriaCreateView.as_view(), name='categoria_create'),
	url(r'(?P<pk>\d+)/$', CategoriaUpdateView.as_view(), name='categoria_update'),
]