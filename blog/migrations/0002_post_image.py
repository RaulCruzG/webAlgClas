# Generated by Django 3.2.15 on 2022-10-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='algoritmo.png', upload_to=''),
        ),
    ]