# ATV09 — Migração do Portal para Django

## Dupla
- Matheus Padilha Cordeiro de Carvalho
- Julio Cesar Ferreira dos Santos

Turma 513 — Desenvolvimento Web

## Descrição
Evolução do portal de currículos e temas (ATV06) para uma aplicação **Django**.
O menu e o conteúdo das páginas deixam de ser HTML fixo e passam a ser cadastrados no **Django Admin**:

- **Conteudo**: `titulo`, `slug`, `conteudo_html` (somente o HTML interno da página) e `ativo`.
- **Menu**: `titulo`, `tipo_destino` (conteúdo interno ou link externo), `ordem`, `ativo`, `conteudo` (FK, quando interno) e `url_externa` (quando externo).
- O menu é gerado dinamicamente pelo banco (context processor) e `header`, `nav`, `main`, `footer` ficam nos templates (`base.html`).
- URLs: `/` (página inicial) e `/conteudo/<slug>/` (conteúdos).
- CSS, imagens e favicon ficam em `portal/static/portal/`.

## Tecnologias
Python 3, Django, SQLite, HTML semântico, CSS (Flexbox e Media Queries) e Git/GitHub.

## Como executar

```bash
# 1. Ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 2. Dependências
pip install -r requirements.txt

# 3. Migrations (já criam os dados iniciais: 5 conteúdos, 2 links externos e 7 itens de menu)
python manage.py migrate

# 4. Superusuário
python manage.py createsuperuser

# 5. Servidor
python manage.py runserver
```

## Acessos
- Aplicação: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

No Admin, ao alterar/ativar/desativar/reordenar `Menu` ou `Conteudo`, o portal é atualizado automaticamente.

## Observações
- Imagens no HTML do banco usam o caminho estático, por exemplo `<img src="/static/portal/img/eu.jpg">`.
- O HTML do banco é exibido com `|safe`; somente administradores devem editá-lo.
