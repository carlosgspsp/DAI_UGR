# Generated by Django 4.1.1 on 2022-11-30 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('preparación', models.TextField(max_length=5000)),
                ('foto', models.FileField(upload_to='media/fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('unidades', models.CharField(max_length=5)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.receta')),
            ],
        ),
    ]
