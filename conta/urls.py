from django.conf.urls import url

from .views import ContaListView, ContaCreateView, ContaUpdateView


urlpatterns = [
	url(r'list/$', ContaListView.as_view(), name='conta_list'),
	url(r'cad/$', ContaCreateView.as_view(), name='conta_create'),
	url(r'(?P<pk>\d+)/$', ContaUpdateView.as_view(), name='conta_update'),
]