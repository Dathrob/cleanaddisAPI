# Generated by Django 3.2.12 on 2022-04-16 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanaddisAPI', '0005_auto_20220416_0626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waste',
            old_name='bought_by',
            new_name='buyer',
        ),
        migrations.RenameField(
            model_name='waste',
            old_name='user',
            new_name='seller',
        ),
    ]