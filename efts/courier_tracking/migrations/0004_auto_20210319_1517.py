# Generated by Django 2.2 on 2021-03-19 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier_tracking', '0003_auto_20210308_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='CourierId',
            new_name='Courier_Id',
        ),
        migrations.RenameField(
            model_name='billing',
            old_name='weight',
            new_name='Weight',
        ),
    ]
