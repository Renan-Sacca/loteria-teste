# Generated by Django 2.1.4 on 2020-10-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0008_auto_20201022_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rifa',
            name='id_skin',
        ),
        migrations.AddField(
            model_name='rifa',
            name='id_skin',
            field=models.ManyToManyField(related_name='skin', to='rifas.skin'),
        ),
    ]
