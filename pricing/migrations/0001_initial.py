# Generated by Django 5.0.6 on 2024-06-26 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoQuarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_quarto', models.CharField(max_length=50)),
                ('preco_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
                ('quartos_disponiveis', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='AjustePreco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('fator_ajuste', models.FloatField()),
                ('preco_ajustado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.tipoquarto')),
            ],
        ),
    ]