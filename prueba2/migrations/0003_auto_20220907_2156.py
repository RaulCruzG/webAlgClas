# Generated by Django 3.2.15 on 2022-09-08 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prueba2', '0002_rename_campos_entero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entero',
            old_name='variable1',
            new_name='variableE1',
        ),
        migrations.RenameField(
            model_name='entero',
            old_name='variable2',
            new_name='variableE2',
        ),
        migrations.RenameField(
            model_name='entero',
            old_name='variable3',
            new_name='variableE3',
        ),
    ]
