# coding: utf-8
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


def _send(from_email, to, subject='', text_content='', html_content='', reply_to=None):
    try:
        if not isinstance(to, (list, tuple)):
            to = (to,)
        kwargs = dict(
            to=to,
            from_email=from_email,
            subject=subject,
            body=text_content,
            alternatives=((html_content, 'text/html'),)
        )
        if reply_to:
            kwargs['headers'] = {'Reply-To': reply_to}
        #if not settings.DEBUG:
        #    kwargs['bcc'] = (settings.RECORDS_EMAIL,)
        message = EmailMultiAlternatives(**kwargs)
        message.send(fail_silently=True)

        return True

    except Exception, e:
        raise Exception('erro: _send() %s' % e.message)
        return False


def enviar_email_padrao(from_email=None, to=None, subject=None, text=None):
    try:
        html = get_template('core/email_padrao.html')
        d = Context({ 'text': text })
        html_content = html.render(d)
        return _send(from_email, [to], subject, '', html_content, from_email)
    except Exception, e:
        print 'erro: enviar_email_padrao()'
        print e.message
        return False
