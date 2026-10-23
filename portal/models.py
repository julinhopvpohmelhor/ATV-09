from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# Slug do Conteudo que funciona como pagina inicial ("/")
SLUG_INICIO = 'inicio'


class Conteudo(models.Model):
    """Pagina do portal. Guarda somente o HTML interno (sem html/head/body/header/nav/footer)."""

    titulo = models.CharField('título', max_length=100)
    slug = models.SlugField('slug', max_length=100, unique=True,
                            help_text='Usado na URL: /conteudo/<slug>/')
    conteudo_html = models.TextField('conteúdo HTML',
                                     help_text='Apenas o HTML interno da página.')
    ativo = models.BooleanField('ativo', default=True)

    class Meta:
        verbose_name = 'conteúdo'
        verbose_name_plural = 'conteúdos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        if self.slug == SLUG_INICIO:
            return reverse('home')
        return reverse('conteudo', args=[self.slug])


class Menu(models.Model):
    """Item da navegacao: aponta para um Conteudo interno ou para uma URL externa."""

    DESTINO_INTERNO = 'interno'
    DESTINO_EXTERNO = 'externo'
    TIPOS_DESTINO = [
        (DESTINO_INTERNO, 'Conteúdo interno'),
        (DESTINO_EXTERNO, 'Link externo'),
    ]

    titulo = models.CharField('título', max_length=60)
    tipo_destino = models.CharField('tipo de destino', max_length=10,
                                    choices=TIPOS_DESTINO, default=DESTINO_INTERNO)
    ordem = models.PositiveIntegerField('ordem', default=0)
    ativo = models.BooleanField('ativo', default=True)
    conteudo = models.ForeignKey(Conteudo, verbose_name='conteúdo relacionado',
                                 on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='itens_menu',
                                 help_text='Obrigatório quando o destino for conteúdo interno.')
    url_externa = models.URLField('URL externa', blank=True,
                                  help_text='Obrigatória quando o destino for link externo.')

    class Meta:
        verbose_name = 'item de menu'
        verbose_name_plural = 'itens de menu'
        ordering = ['ordem', 'titulo']

    def __str__(self):
        return self.titulo

    @property
    def externo(self):
        return self.tipo_destino == self.DESTINO_EXTERNO

    def clean(self):
        if self.tipo_destino == self.DESTINO_INTERNO:
            if not self.conteudo_id:
                raise ValidationError({'conteudo': 'Escolha o conteúdo relacionado.'})
            self.url_externa = ''
        else:
            if not self.url_externa:
                raise ValidationError({'url_externa': 'Informe a URL externa.'})
            self.conteudo = None
