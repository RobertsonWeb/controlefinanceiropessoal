#coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Conta(models.Model):
    descricao = models.CharField(u'Descrição', max_length=40)
    saldo = models.DecimalField('Saldo', max_digits=10, decimal_places=2, default=0)

    def __unicode__(self):
        return '%s: R$ %d' % (self.descricao, self.saldo)

    class Meta:
        ordering = ['-saldo','descricao']

    @property
    def get_absolute_url(self):
        return reverse('conta_update', args=[str(self.id)])