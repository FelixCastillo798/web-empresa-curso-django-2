# Generated by Django 2.0.2 on 2019-09-21 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
