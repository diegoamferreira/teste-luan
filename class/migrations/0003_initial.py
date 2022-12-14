# Generated by Django 4.1 on 2022-08-23 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('class', '0002_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField(verbose_name='Data do Evento')),
                ('salario', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('habilitado', models.BooleanField(blank=True, default=True)),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de Criação')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
