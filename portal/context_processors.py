from .views import obter_itens_menu


def menu(request):
    """Deixa o menu disponivel em todos os templates como {{ itens_menu }}."""
    return {'itens_menu': obter_itens_menu()}
