# Generated by Django 2.0.7 on 2018-08-31 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Entradas'},
        ),
    ]
