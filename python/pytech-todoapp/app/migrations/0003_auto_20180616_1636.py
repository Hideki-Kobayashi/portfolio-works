# Generated by Django 2.0.6 on 2018-06-16 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180616_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='dealine',
            new_name='deadline',
        ),
    ]
