# Generated by Django 2.1.4 on 2020-10-23 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0007_auto_20201022_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifa',
            name='id_skin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='skin', to='rifas.skin'),
        ),
    ]
