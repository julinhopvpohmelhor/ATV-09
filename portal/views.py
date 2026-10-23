from django.shortcuts import get_object_or_404, render

from .models import SLUG_INICIO, Conteudo, Menu


def obter_itens_menu():
    """Itens ativos do menu, na ordem definida no Admin.

    Itens internos so aparecem se o Conteudo relacionado existir e estiver ativo.
    """
    itens = Menu.objects.filter(ativo=True).select_related('conteudo')
    return [
        item for item in itens
        if item.externo or (item.conteudo and item.conteudo.ativo)
    ]


def home(request):
    """Pagina inicial: exibe o Conteudo com slug 'inicio' (se estiver ativo)."""
    conteudo = Conteudo.objects.filter(slug=SLUG_INICIO, ativo=True).first()
    return render(request, 'portal/conteudo.html', {'conteudo': conteudo})


def conteudo_detalhe(request, slug):
    """Exibe um Conteudo ativo, buscado pelo slug da URL."""
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'portal/conteudo.html', {'conteudo': conteudo})
