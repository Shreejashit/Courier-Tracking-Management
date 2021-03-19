# Generated by Django 2.2 on 2021-03-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courier_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourierId', models.IntegerField(max_length=5)),
                ('From_Name', models.CharField(max_length=20)),
                ('From_EmailAddress', models.CharField(max_length=20)),
                ('From_Gender', models.CharField(max_length=10)),
                ('From_Age', models.CharField(max_length=10)),
                ('From_Address', models.CharField(max_length=30)),
                ('From_Mobile', models.CharField(max_length=20)),
                ('To_Name', models.CharField(max_length=20)),
                ('To_Gender', models.CharField(max_length=10)),
                ('To_Address', models.CharField(max_length=30)),
                ('To_Mobile', models.CharField(max_length=20)),
                ('Product_Name', models.CharField(max_length=20)),
                ('Weight', models.CharField(max_length=10)),
                ('Price', models.CharField(max_length=10)),
            ],
        ),
    ]
