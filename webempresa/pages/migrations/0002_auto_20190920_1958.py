# Generated by Django 2.0.2 on 2019-09-21 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
    ]
