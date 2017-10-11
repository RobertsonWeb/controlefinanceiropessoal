# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Usuario(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('ADMINISTRADOR', 'Administrador'),
        ('COMUM', 'Comum' )
    )

    USERNAME_FIELD = 'email'

    nome = models.CharField(_(u'nome'), max_length=70)
    email = models.EmailField(_('email'), unique=True, max_length=70, db_index=True)
    is_active = models.BooleanField(_(u'ativo'), default=False, help_text='Se ativo o usuário tem permissão para acessar o sistema')
    tipo = models.CharField(_(u'tipo do usuário'), max_length=15, choices=TIPOS, default='COMUM')

    objects = UserManager()

    class Meta:
        ordering            =   [u'nome']
        verbose_name        =   _(u'usuário')
        verbose_name_plural =   _(u'usuários')

    def __unicode__(self):
        return self.nome

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.nome[0:10].strip()

    def get_full_name(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRADOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('usuario_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuario_delete', args=[str(self.id)])


