# Generated by Django 4.0.6 on 2022-07-12 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_solicitacoes_impressora_solicitacoes_marca_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitacoes',
            old_name='setor',
            new_name='modelo',
        ),
    ]
