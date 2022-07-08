# Generated by Django 4.0.6 on 2022-07-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impressoras',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('setor', models.CharField(blank=True, max_length=50, null=True)),
                ('marca', models.CharField(blank=True, max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, max_length=100, null=True)),
                ('qtd_toners', models.IntegerField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]