from django.db import migrations

# Dados iniciais (conteudo minimo da ATV09): 5 conteudos internos (1 e a pagina
# inicial), 2 links externos e 7 itens de menu. Tudo pode ser editado no Django Admin.

CONTEUDOS = [
    ('Início', 'inicio', '<section class="conteudo">\n<h1>Curriculos e Temas</h1>\n<article class="conteudo"> \n            <h5> Matheus Padilha Cordeiro de Carvalho </h5>\n            <img class="fotinha" src="/static/portal/img/eu.jpg"> \n        </article>\n<article class="conteudo">\n            <h5> Julio Cesar Ferreira dos Santos </h5>\n            <img class="fotinha" src="/static/portal/img/cesinha.jpeg"> \n        </article>\n</section>'),
    ('Currículo de Matheus', 'curriculo-matheus', '<section class="conteudo">\n<h1>Currículo</h1>\n<article id="perfil">\n\n        <div class="Foto">\n            <img src="/static/portal/img/eu.jpg" alt="Foto do curriculo" title="Foto do Candidato">\n        </div>\n\n        <div class="dados">\n            <h2> Matheus Padilha;</h2>\n            <h2> Desenvolvedor / Estudante de TI;</h2>\n            <h2> Bom Conselho ( Pe );</h2>\n            <h2> mppc1@aluno.ifal.edu.br;</h2>\n            <h2> (01) 0101010101.</h2>\n        </div>\n    </article>\n<article id="objetivo">\n        <h2>Objetivo</h2>\n        <h3>Técnico em TI em busca de oportunidade para desenvolver habilidades em programação, suporte técnico e desenvolvimento de sistemas, com foco em aprendizado e crescimento profissional.</h3>\n    </article>\n<article id="formacao">\n        <h2>Formação</h2>\n        <h3>Cursando Técnico em Informática</h3>\n\n        <br><br>\n\n        <h2>Habilidades</h2>\n        <ul>\n            <li>Trabalho em Grupo;</li>\n            <li>Comunicativo;</li>\n            <li>Liderança.</li>\n        </ul>\n    </article>\n</section>'),
    ('Currículo de Julio', 'curriculo-julio', '<section class="conteudo">\n<h1>Currículo</h1>\n<article id="perfil">\n\n    <div  class="Foto">\n        <img src="/static/portal/img/cesinha.jpeg" alt="Foto do curriculo" title="Foto do Candidato"> \n    </div>\n\n    <div class="dados">\n        <h2> Julio Cesar Ferreira dos Santos;</h2>\n        <h2> Desenvolvedor / Estudante de TI;</h2>\n        <h2> Taquarana ( Al );</h2>\n        <h2> jcfs9@aluno.ifal.edu.br;</h2>\n        <h2> (02) 0202020202. </h2>\n    </div>\n</article>\n<article id="objetivo">\n    <h2>Objetivo</h2>\n    <h3> Atuar na area de tecnologia e aprender cada vez mais sobre informatica. </h3>\n</article>\n<article id="formacao">\n    <h2>Formação</h2>\n    <h3> Cursando Tecnico em Informatica </h3>\n\n    <br><br>\n\n    <h2>Habilidades</h2>\n    <ul>\n        <li>Trabalho em Equipe;</li>\n        <li>Facilidade para aprender;</li>\n        <li>Conhecimento em jogos;</li>\n        <li>Bom e Novo.</li>\n    </ul>\n</article>\n</section>'),
    ('Tema de Matheus', 'tema-matheus', '<section class="conteudo">\n<h1>Jogos de Matheus</h1>\n<article class="box">\n    <img src="/static/portal/img/val.jpg" alt="Logo do Valorant" title="Logo do Valorant">\n\n    <div class="informacoes">\n        <h2> Valorant </h2>\n        <h3> Riot Games </h3>\n        <h3> FPS com poderes</h3>\n        <h3> <a href="https://playvalorant.com/pt-br/download/" target="_blank"> Download </a></h3>\n    </div>\n</article>\n<article class="box1">\n    <img src="/static/portal/img/fort.jpg" alt="Logo do Fortinite" title="Logo do Fortnite">\n\n    <div class="informacoes">\n        <h2> Fortnite </h2>\n        <h3> Epic Games </h3>\n        <h3> BattleRoyale </h3>\n        <h3> <a href="https://www.fortnite.com/download?lang=pt-BR" target="_blank"> Download </a></h3>\n    </div>\n</article>\n<article class="box1">\n    <img src="/static/portal/img/rdr.jpg" alt="Logo do Read Dead Remdeption 2" title="Logo do Read Dead Remdemption 2">\n\n    <div class="informacoes">\n        <h2> Read Dead Remdemption </h2>\n        <h3> Rock Star</h3>\n        <h3> Modo Historia </h3>\n        <h3> <a href="https://www.rockstargames.com/br/reddeadredemption2" target="_blank"> Download </a></h3>\n    </div>\n</article>\n</section>'),
    ('Tema de Julio', 'tema-julio', '<section class="conteudo">\n<h1>Jogos de Julio</h1>\n<article class="box">\n    <img src="/static/portal/img/minecraft.jpg" alt="Logo do Minecraft" title="Logo do Minecraft">\n\n    <div class="informacoes">\n        <h2> Minecraft </h2>\n        <h3> Mojang Studios </h3>\n        <h3> Survival com estilo quadrado </h3>\n        <h3> <a href="https://www.minecraft.net/pt-br/store/minecraft-deluxe-collection-pc" target="_blank"> Download </a></h3>\n    </div>\n</article>\n<article class="box1">\n    <img src="/static/portal/img/terraria.jpg" alt="Logo do Terraria" title="Logo do Terraria">\n\n    <div class="informacoes">\n        <h2> Terraria </h2>\n        <h3> Re-Logic </h3>\n        <h3> é um jogo de ação e aventura em 2D que combina elementos de sobrevivência, construção (sandbox) e RPG </h3>\n        <h3> <a href="https://store.steampowered.com/app/105600/Terraria/" target="_blank"> Download </a></h3>\n    </div>\n</article>\n<article class="box1">\n    <img src="/static/portal/img/val.jpg" alt="Logo do Valorant" title="Logo do Valorant">\n\n    <div class="informacoes">\n        <h2> Valorant </h2>\n        <h3> Riot Games </h3>\n        <h3> FPS com podres </h3>\n        <h3> <a href="https://playvalorant.com/pt-br/download/" target="_blank"> Download </a></h3>\n    </div>\n</article>\n<article class="box1">\n    <img src="/static/portal/img/ark.jpg" alt="Logo do Ark: Survival Evolved" title="Logo do Ark: Survival Evolved">\n\n    <div class="informacoes">\n        <h2> Ark: Survival Evolved </h2>\n        <h3> Studio Wildcard </h3>\n        <h3> ação, aventura e sobrevivência em mundo aberto com dinossauros </h3>\n        <h3> <a href="https://store.steampowered.com/app/346110/ARK_Survival_Evolved/" target="_blank"> Download </a></h3>\n    </div>\n</article>\n</section>'),
]

MENUS = [
    # (titulo, ordem, slug do conteudo ou None, url externa)
    ('Início', 1, 'inicio', ''),
    ('Currículo de Matheus', 2, 'curriculo-matheus', ''),
    ('Currículo de Julio', 3, 'curriculo-julio', ''),
    ('Tema de Matheus', 4, 'tema-matheus', ''),
    ('Tema de Julio', 5, 'tema-julio', ''),
    ('GitHub', 6, None, 'https://github.com'),
    ('W3Schools', 7, None, 'https://www.w3schools.com'),
]


def criar_dados(apps, schema_editor):
    Conteudo = apps.get_model('portal', 'Conteudo')
    Menu = apps.get_model('portal', 'Menu')

    por_slug = {}
    for titulo, slug, html in CONTEUDOS:
        por_slug[slug] = Conteudo.objects.create(titulo=titulo, slug=slug, conteudo_html=html, ativo=True)

    for titulo, ordem, slug, url in MENUS:
        if slug:
            Menu.objects.create(titulo=titulo, tipo_destino='interno', ordem=ordem,
                                ativo=True, conteudo=por_slug[slug])
        else:
            Menu.objects.create(titulo=titulo, tipo_destino='externo', ordem=ordem,
                                ativo=True, url_externa=url)


def remover_dados(apps, schema_editor):
    apps.get_model('portal', 'Menu').objects.filter(titulo__in=[m[0] for m in MENUS]).delete()
    apps.get_model('portal', 'Conteudo').objects.filter(slug__in=[c[1] for c in CONTEUDOS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_dados, remover_dados),
    ]
