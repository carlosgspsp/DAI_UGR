# Generated by Django 4.1.1 on 2022-11-30 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='foto',
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='media/fotos')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.receta')),
            ],
        ),
    ]
