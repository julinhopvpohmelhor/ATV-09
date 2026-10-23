import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='título')),
                ('slug', models.SlugField(help_text='Usado na URL: /conteudo/<slug>/', max_length=100, unique=True, verbose_name='slug')),
                ('conteudo_html', models.TextField(help_text='Apenas o HTML interno da página.', verbose_name='conteúdo HTML')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
            ],
            options={
                'verbose_name': 'conteúdo',
                'verbose_name_plural': 'conteúdos',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60, verbose_name='título')),
                ('tipo_destino', models.CharField(choices=[('interno', 'Conteúdo interno'), ('externo', 'Link externo')], default='interno', max_length=10, verbose_name='tipo de destino')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='ordem')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('url_externa', models.URLField(blank=True, help_text='Obrigatória quando o destino for link externo.', verbose_name='URL externa')),
                ('conteudo', models.ForeignKey(blank=True, help_text='Obrigatório quando o destino for conteúdo interno.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itens_menu', to='portal.conteudo', verbose_name='conteúdo relacionado')),
            ],
            options={
                'verbose_name': 'item de menu',
                'verbose_name_plural': 'itens de menu',
                'ordering': ['ordem', 'titulo'],
            },
        ),
    ]
