# Generated by Django 3.0.8 on 2020-08-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizaa', '0002_auto_20200803_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customerid', models.AutoField(primary_key=True, serialize=False)),
                ('PhoneNumber', models.PositiveIntegerField()),
            ],
        ),
    ]